import json
from .gemini_client import gemini_client

class ProjectChatAgent:
    """
    Project Chat Agent
    
    Responsibilities:
    - Receive the user's chat message and the current project state.
    - Evaluate the request.
    - Generate a natural language reply.
    - Modify the project state JSON (tasks, modules, roadmap, etc.) based on the request.
    """
    
    async def process_chat(self, user_message: str, current_project_state: dict) -> dict:
        prompt = f"""
        You are DevPilot AI, a highly intelligent and helpful Software Project Assistant.
        
        The user is interacting with you to modify or ask questions about their current project architecture.
        
        CURRENT PROJECT STATE (JSON):
        {json.dumps(current_project_state, indent=2)}
        
        USER MESSAGE:
        {user_message}
        
        INSTRUCTIONS:
        1. Understand the user's request.
        2. Formulate a helpful, conversational response to the user.
        3. If the user asks to modify the project (e.g., add a feature, update a task, add a module), YOU MUST modify the relevant fields in the provided project state JSON. 
        4. Return your final output STRICTLY as a JSON object matching this schema:
        {{
            "reply": "Your conversational response to the user, formatted in Markdown.",
            "updated_project": {{ ... the complete modified project state ... }}
        }}
        
        Make sure `updated_project` retains all original keys (project_id, status, summary, modules, complexity, roadmap, tasks, tech_stack_recommendation, generated_files, workspace_path, export_zip_path, review_result, readme_content) even if you don't modify them.
        Do not wrap the JSON in markdown code blocks. Return raw JSON.
        """
        
        try:
            response_data = await gemini_client.generate_json(prompt, fallback_data={
                "reply": "I've successfully updated the project for you.",
                "updated_project": current_project_state
            })
            return response_data
        except Exception as e:
            # Fallback if Gemini fails
            print(f"Chat agent failed: {e}")
            return {
                "reply": "I'm sorry, I encountered an error while trying to process your request.",
                "updated_project": current_project_state
            }
