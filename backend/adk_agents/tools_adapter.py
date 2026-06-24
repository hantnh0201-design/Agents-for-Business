from backend.mcp.tools import (
    create_project_workspace,
    create_folder,
    write_file,
    read_file,
    list_directory,
    create_zip_export
)

# In Google ADK, tools can be standard python functions wrapped via the SDK or used directly 
# depending on the specific ADK class (e.g. adk.Tool, or callable type hinting).
# We expose them here directly for integration with ADK agents.

class ADKToolsAdapter:
    """
    Adapts our physical MCP filesystem tools into callable constructs for the Google ADK.
    """
    @staticmethod
    def create_project_workspace_tool(project_id: str) -> str:
        """Creates the base workspace directory for a project."""
        return create_project_workspace(project_id)

    @staticmethod
    def create_folder_tool(project_id: str, folder_path: str) -> str:
        """Creates a subfolder within the project workspace."""
        return create_folder(project_id, folder_path)

    @staticmethod
    def write_file_tool(project_id: str, file_path: str, content: str) -> str:
        """Writes content to a file inside the project workspace."""
        return write_file(project_id, file_path, content)

    @staticmethod
    def read_file_tool(project_id: str, file_path: str) -> str:
        """Reads content from a file inside the project workspace."""
        return read_file(project_id, file_path)

    @staticmethod
    def list_directory_tool(project_id: str, folder_path: str = "") -> str:
        """Lists all files and folders in a specific directory within the workspace."""
        return list_directory(project_id, folder_path)

    @staticmethod
    def create_zip_export_tool(project_id: str) -> str:
        """Zips the entire workspace for export."""
        return create_zip_export(project_id)
