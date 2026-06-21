from fastapi import FastAPI, HTTPException
from models.schemas import (
    HealthResponse,
    GenerateRequest,
    GenerateResponse,
    ProjectResponse,
    ProjectFilesResponse,
    ExportResponse,
    ErrorResponse
)

app = FastAPI(
    title="DevPilot AI Backend",
    description="RESTful APIs for DevPilot AI Project Manager Agent",
    version="1.0.0"
)

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
    # Mock response. AI logic to be implemented later.
    return GenerateResponse(
        project_id="12345",
        status="success",
        summary="Online Flower Shop",
        roadmap=[
            "Requirement Analysis",
            "Database Design",
            "Frontend Development",
            "Backend Development",
            "Testing",
            "Deployment"
        ]
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
