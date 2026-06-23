from .planner_agent import PlannerAgent
from .task_agent import TaskManagerAgent
from .tech_agent import TechAdvisorAgent
from .code_agent import CodeGeneratorAgent
from .reviewer_agent import ReviewerAgent
from .documentation_agent import DocumentationAgent
from mcp.tools import create_zip_export
import uuid

class MainOrchestratorAgent:
    """
    Main Orchestrator Agent
    
    Responsibilities:
    - Receive user requests.
    - Initialize the multi-agent workflow.
    - Call specialized agents in the correct sequential order.
    - Combine outputs from all agents.
    - Return the final project package result.
    """
    
    def __init__(self):
        # Initialize all the specialized agents
        self.planner = PlannerAgent()
        self.task_manager = TaskManagerAgent()
        self.tech_advisor = TechAdvisorAgent()
        self.code_generator = CodeGeneratorAgent()
        self.reviewer = ReviewerAgent()
        self.documentation = DocumentationAgent()

    async def execute_workflow(self, user_request: dict) -> dict:
        """
        Executes the full agentic workflow sequentially.
        """
        # Generate a unique dynamic project ID for the workspace
        project_id = f"proj_{uuid.uuid4().hex[:8]}"
        
        # 1. Planner Agent analyzes the core requirements
        project_summary = await self.planner.analyze_project(user_request)
        
        # 2. Task Manager Agent breaks the project into logical milestones
        task_list = await self.task_manager.generate_tasks(project_summary)
        
        # 3. Tech Advisor Agent chooses the best technologies based on the tasks
        tech_stack = await self.tech_advisor.recommend_stack(task_list)
        
        # 4. Code Generator Agent scaffolds the application structure AND runs physical MCP actions
        generated_project = await self.code_generator.generate_project(tech_stack, project_id)
        
        # 5. Reviewer Agent ensures the code and structure meet standards
        review_report = await self.reviewer.review_project(generated_project)
        
        # 6. Documentation Agent creates README and guides AND saves it via MCP
        docs = await self.documentation.generate_documentation(review_report, project_id)
        
        # MCP ACTION: Export the final generated workspace as a zip archive
        export_result = await create_zip_export(project_id)
        
        # Extract roadmap and tasks directly from task_result
        roadmap = task_list.get("roadmap", [])
        tasks = task_list.get("tasks", [])
        
        return {
            "project_id": project_id,
            "status": "success",
            "summary": project_summary.get("summary", "Project Initialized"),
            "modules": project_summary.get("modules", []),
            "complexity": project_summary.get("complexity", "Medium"),
            "roadmap": roadmap,
            "tasks": tasks,
            "tech_stack_recommendation": tech_stack,
            "generated_files": generated_project.get("generated_files", []),
            "workspace_path": generated_project.get("workspace_path", ""),
            "export_zip_path": export_result.get("download_url", ""),
            "review_result": review_report,
            "readme_content": docs.get("readme_content", "")
        }
