import os
import json
import logging
from pathlib import Path
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Step 1: Load environment variables from backend/.env using absolute path
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

logger = logging.getLogger(__name__)

class GeminiClient:
    """
    A reusable client class to interact with the Google Gen AI API using the modern google-genai SDK.
    """
    def __init__(self):
        # Step 2: Fetch the API key securely from environment variables (Never hardcoded)
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            logger.warning(f"GEMINI_API_KEY is not set in the environment. API calls will fail. (Tried loading from: {dotenv_path})")
            self.client = None
        else:
            # Step 3: Initialize the genai Client with the provided API key
            self.client = genai.Client(api_key=self.api_key)
            
        # We use gemini-2.5-flash as the default model for quick, structured responses
        self.model_name = "gemini-2.5-flash"

    async def generate_text(self, prompt: str, fallback_text: str = "") -> str:
        """
        Sends a prompt to Gemini and returns the generated text.
        If an error occurs or the client is not initialized, it returns the fallback_text.
        """
        if not self.client:
            return fallback_text
            
        try:
            print("Calling Gemini...")
            # Step 4: Call the async version of generate_content
            response = await self.client.aio.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            print("Gemini response received")
            logger.info(f"Successfully generated text using {self.model_name}.")
            return response.text
        except Exception as e:
            print(f"Gemini API Error: {e}. Using fallback data.")
            logger.error(f"Error generating text with Gemini: {e}")
            return fallback_text

    async def generate_json(self, prompt: str, fallback_data: dict) -> dict:
        """
        Sends a prompt to Gemini expecting a JSON response and parses it into a dictionary.
        If an error occurs or parsing fails, it returns the fallback_data.
        """
        if not self.client:
            return fallback_data
            
        try:
            print("Calling Gemini...")
            # Step 5: Enforce JSON format in the prompt
            full_prompt = prompt + "\n\nIMPORTANT: Return ONLY valid JSON. Do not use markdown code blocks like ```json."
            
            # Step 6: Use GenerateContentConfig to enforce application/json response type natively
            response = await self.client.aio.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            
            print("Gemini response received")
            logger.info(f"Successfully generated JSON using {self.model_name}.")
            text = response.text.strip()
            
            # Step 7: Clean up residual markdown if the model accidentally included it
            if text.startswith("```json"):
                text = text[7:]
            if text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
                
            # Step 8: Parse and return the JSON dictionary
            return json.loads(text.strip())
        except Exception as e:
            # Step 9: Catch any failure and return fallback mock data instead of crashing
            print(f"Gemini API Error: {e}. Using fallback data.")
            logger.error(f"Error generating JSON with Gemini: {e}")
            return fallback_data

# Create a singleton instance to be used across the application
gemini_client = GeminiClient()
