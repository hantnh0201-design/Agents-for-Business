from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class HealthResponse(BaseModel):
    status: str

class GenerateRequest(BaseModel):
    project_name: str
    description: str
    tech_stack: str

class GenerateResponse(BaseModel):
    project_id: str
    status: str
    summary: str
    modules: List[str]
    complexity: str
    roadmap: List[str]
    tasks: List[Dict[str, Any]]
    tech_stack_recommendation: Dict[str, Any]
    generated_files: List[Dict[str, Any]]
    workspace_path: Optional[str] = None
    export_zip_path: Optional[str] = None
    review_result: Dict[str, Any]
    readme_content: str

class ProjectResponse(BaseModel):
    project_id: str
    name: str
    status: str

class ProjectFilesResponse(BaseModel):
    files: List[str]

class ExportResponse(BaseModel):
    download_url: str

class ErrorResponse(BaseModel):
    status: str
    message: str
