from .gemini_client import GeminiClient
from mcp.tools import create_project_workspace, create_folder, write_file

class CodeGeneratorAgent:
    """
    Code Generator Agent
    
    Responsibilities:
    - Generate starter project structure.
    - Generate initial source code.
    - Generate configuration files.
    - Execute real filesystem actions via MCP tools.
    """

    def __init__(self):
        self.gemini = GeminiClient()

    async def generate_project(self, tech_stack: dict, project_id: str) -> dict:
        """
        Generates the starter project structure and code files based on the chosen stack,
        and uses MCP tools to actually scaffold these files in the file system.
        """
        # MCP ACTION 1: Create the secure workspace for this project
        await create_project_workspace(project_id)
        
        # MCP ACTION: Explicitly create essential directory structures
        await create_folder(project_id, "frontend/src")
        await create_folder(project_id, "backend")
        
        fallback = {
            "generated_files": [
                {"path": "frontend/src/App.tsx", "purpose": "Main React entry component", "content": "export default function App() { return <div>Hello World</div>; }"},
                {"path": "backend/main.py", "purpose": "FastAPI application entry point", "content": "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef read_root(): return {'status': 'ok'}"},
                {"path": "backend/requirements.txt", "purpose": "Backend Python dependencies", "content": "fastapi\nuvicorn"},
                {"path": "README.md", "purpose": "Project documentation", "content": "# Project Title\n"},
                {"path": ".env.example", "purpose": "Environment variables template", "content": "PORT=8000\n"},
                {"path": "docker-compose.yml", "purpose": "Container orchestration", "content": "version: '3'\n"}
            ]
        }
        
        prompt = f"""
        You are an expert Software Engineer.
        Given the following technology stack, generate an initial folder and file structure for the project.
        
        Tech Stack:
        {tech_stack}
        
        Return a JSON object with:
        - "generated_files": An array of objects representing the files to be created. Each object must contain:
            - "path": The file path (e.g. "backend/app/main.py").
            - "purpose": A short string explaining the purpose of the file.
            - "content": An initial functional starter code snippet or template text to be written into the file.
        Generate at least the following essential files along with their code:
        - README.md
        - frontend/src/App.tsx
        - backend/main.py
        - backend/requirements.txt
        """
        
        # Get the AI-generated plan containing file paths and contents
        ai_plan = await self.gemini.generate_json(prompt, fallback)
        files = ai_plan.get("generated_files", [])
        
        written_files = []
        
        # MCP ACTION 2: Act on the physical file system
        # The AI agent loops through the plan and instructs the MCP to write each file.
        for file_info in files:
            file_path = file_info.get("path")
            content = file_info.get("content", f"# Starter template for {file_path}")
            
            # Execute physical write_file tool
            result = await write_file(project_id, file_path, content)
            
            if result["status"] == "success":
                written_files.append({"path": file_path, "purpose": file_info.get("purpose")})

        return {
            "workspace_path": f"backend/generated_projects/{project_id}",
            "generated_files": written_files
        }
