from pydantic import BaseModel
from typing import List, Optional

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
    roadmap: List[str]

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
