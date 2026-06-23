import os
import shutil
import logging
import zipfile
from typing import Dict, Any

logger = logging.getLogger(__name__)

# Base directory for all generated projects
GENERATED_PROJECTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generated_projects'))

def _get_safe_path(project_id: str, relative_path: str = "") -> str:
    """
    Validates the path to ensure it doesn't escape the generated_projects/project_id directory.
    This fulfills the security rules to reject absolute paths and '..'.
    """
    if ".." in relative_path or relative_path.startswith("/") or relative_path.startswith("\\") or os.path.isabs(relative_path):
        raise ValueError("Invalid path. Absolute paths and directory traversal ('..') are strictly prohibited.")
    
    project_dir = os.path.join(GENERATED_PROJECTS_DIR, project_id)
    safe_path = os.path.abspath(os.path.join(project_dir, relative_path))
    
    # Final security check to ensure no writing outside generated_projects
    if not safe_path.startswith(project_dir):
        raise ValueError("Invalid path. Attempted to access files outside the project workspace.")
        
    return safe_path

async def create_project_workspace(project_id: str) -> Dict[str, Any]:
    """
    MCP Action: Creates the main project workspace folder where all generated code will reside.
    """
    try:
        project_dir = _get_safe_path(project_id)
        os.makedirs(project_dir, exist_ok=True)
        return {"status": "success", "message": f"Workspace created for project {project_id}", "path": project_dir}
    except Exception as e:
        logger.error(f"Failed to create workspace for {project_id}: {e}")
        return {"status": "error", "message": str(e)}

async def create_folder(project_id: str, folder_path: str) -> Dict[str, Any]:
    """
    MCP Action: Creates a nested directory inside the project workspace safely.
    """
    try:
        safe_path = _get_safe_path(project_id, folder_path)
        os.makedirs(safe_path, exist_ok=True)
        return {"status": "success", "message": f"Folder '{folder_path}' created successfully."}
    except Exception as e:
        logger.error(f"Failed to create folder '{folder_path}': {e}")
        return {"status": "error", "message": str(e)}

async def write_file(project_id: str, file_path: str, content: str) -> Dict[str, Any]:
    """
    MCP Action: Writes generated AI code/text into a physical file within the workspace.
    """
    try:
        safe_path = _get_safe_path(project_id, file_path)
        # Ensure the parent directory exists
        os.makedirs(os.path.dirname(safe_path), exist_ok=True)
        
        with open(safe_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return {"status": "success", "message": f"File '{file_path}' written successfully.", "path": safe_path}
    except Exception as e:
        logger.error(f"Failed to write file '{file_path}': {e}")
        return {"status": "error", "message": str(e)}

async def read_file(project_id: str, file_path: str) -> Dict[str, Any]:
    """
    MCP Action: Reads an existing file's contents from the workspace.
    """
    try:
        safe_path = _get_safe_path(project_id, file_path)
        if not os.path.exists(safe_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")
            
        with open(safe_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return {"status": "success", "content": content}
    except Exception as e:
        logger.error(f"Failed to read file '{file_path}': {e}")
        return {"status": "error", "message": str(e)}

async def list_directory(project_id: str, folder_path: str = "") -> Dict[str, Any]:
    """
    MCP Action: Lists the files and directories inside the project workspace.
    """
    try:
        safe_path = _get_safe_path(project_id, folder_path)
        if not os.path.exists(safe_path):
            return {"status": "success", "items": []}
            
        items = os.listdir(safe_path)
        return {"status": "success", "items": items}
    except Exception as e:
        logger.error(f"Failed to list directory '{folder_path}': {e}")
        return {"status": "error", "message": str(e)}

async def create_zip_export(project_id: str) -> Dict[str, Any]:
    """
    MCP Action: Packages the entire generated project folder into a downloadable zip file.
    """
    try:
        project_dir = _get_safe_path(project_id)
        if not os.path.exists(project_dir):
            raise FileNotFoundError("Project workspace does not exist.")
            
        zip_path = os.path.abspath(os.path.join(GENERATED_PROJECTS_DIR, f"{project_id}.zip"))
        
        # Create zip archive. make_archive adds the .zip extension automatically.
        shutil.make_archive(zip_path.replace('.zip', ''), 'zip', project_dir)
        
        return {"status": "success", "message": f"Exported project {project_id}", "download_url": f"/downloads/{project_id}.zip"}
    except Exception as e:
        logger.error(f"Failed to create zip export for {project_id}: {e}")
        return {"status": "error", "message": str(e)}
