from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import (
    HealthResponse,
    GenerateRequest,
    GenerateResponse,
    ProjectResponse,
    ProjectFilesResponse,
    ExportResponse,
    ErrorResponse
)
from agents.orchestrator import MainOrchestratorAgent

app = FastAPI(
    title="DevPilot AI Backend",
    description="RESTful APIs for DevPilot AI Project Manager Agent",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the main agent
orchestrator = MainOrchestratorAgent()

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Returns the backend status.
    """
    return HealthResponse(status="healthy")

@app.post("/generate", response_model=GenerateResponse)
async def generate_project(request: GenerateRequest):
    """
    Generate a complete software project plan from the user's description.
    """
    # Trigger the agentic workflow with the user request
    workflow_result = await orchestrator.execute_workflow({
        "project_name": request.project_name,
        "description": request.description,
        "tech_stack": request.tech_stack
    })
    
    # Return response based on the workflow execution.
    return GenerateResponse(
        project_id=workflow_result.get("project_id", "12345"),
        status=workflow_result.get("status", "success"),
        summary=workflow_result.get("summary", "Project Summary"),
        modules=workflow_result.get("modules", []),
        complexity=workflow_result.get("complexity", "Medium"),
        roadmap=workflow_result.get("roadmap", []),
        tasks=workflow_result.get("tasks", []),
        tech_stack_recommendation=workflow_result.get("tech_stack_recommendation", {}),
        generated_files=workflow_result.get("generated_files", []),
        workspace_path=workflow_result.get("workspace_path", ""),
        export_zip_path=workflow_result.get("export_zip_path", ""),
        review_result=workflow_result.get("review_result", {}),
        readme_content=workflow_result.get("readme_content", "")
    )

@app.get("/projects/{project_id}", response_model=ProjectResponse, responses={404: {"model": ErrorResponse}})
async def get_project(project_id: str):
    """
    Retrieve project information.
    """
    if project_id != "12345":
        raise HTTPException(status_code=404, detail="Project not found")
        
    return ProjectResponse(
        project_id=project_id,
        name="Flower Shop Website",
        status="Completed"
    )

@app.get("/projects/{project_id}/files", response_model=ProjectFilesResponse, responses={404: {"model": ErrorResponse}})
async def get_project_files(project_id: str):
    """
    Returns generated files.
    """
    if project_id != "12345":
        raise HTTPException(status_code=404, detail="Project not found")
        
    return ProjectFilesResponse(
        files=[
            "README.md",
            "frontend/src/App.tsx",
            "backend/main.py"
        ]
    )

@app.post("/projects/{project_id}/export", response_model=ExportResponse, responses={404: {"model": ErrorResponse}})
async def export_project(project_id: str):
    """
    Export the generated project as a ZIP package.
    """
    if project_id != "12345":
        raise HTTPException(status_code=404, detail="Project not found")
        
    return ExportResponse(
        download_url="/downloads/project.zip"
    )
