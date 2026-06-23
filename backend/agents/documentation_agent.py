from .gemini_client import GeminiClient
from mcp.tools import write_file

class DocumentationAgent:
    """
    Documentation Agent
    
    Responsibilities:
    - Generate README.md.
    - Generate Installation Guide.
    - Generate Deployment Guide.
    - Generate Project Overview.
    - Persist the documentation using MCP.
    """

    def __init__(self):
        self.gemini = GeminiClient()

    async def generate_documentation(self, review_report: dict, project_id: str) -> dict:
        """
        Creates necessary documentation based on the reviewed project structure and code,
        and uses MCP to overwrite the README.md with the high-quality generated content.
        """
        fallback = {
            "readme_content": "# Generated Project\n\nThis project was scaffolded via DevPilot AI.\n\n## Overview\nA robust web application with a separated frontend and backend architecture.\n\n## Setup\nRun `npm install` for frontend, and `pip install -r requirements.txt` for backend.\n\n## Deployment\nDeploy the backend via Google Cloud Run and frontend via Vercel."
        }
        
        prompt = f"""
        You are a highly skilled Technical Writer.
        Based on the code review report and context of the project, generate a comprehensive and detailed README file.
        
        Review Report Context:
        {review_report}
        
        Return a JSON object with:
        - "readme_content": A detailed markdown string for the complete README.md file. It should include Project Overview, Architecture, Tech Stack, Setup Instructions, and Deployment Guide. Ensure the content is rich, professional, and well-structured.
        """
        
        docs = await self.gemini.generate_json(prompt, fallback)
        readme_content = docs.get("readme_content", "")
        
        # MCP ACTION: The agent writes the generated markdown directly to the workspace README.md file
        if readme_content:
            await write_file(project_id, "README.md", readme_content)
        
        return docs
