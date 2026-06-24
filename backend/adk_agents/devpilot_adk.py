"""
Google ADK Integration for DevPilot AI.

This module demonstrates how DevPilot AI leverages the Google Agent Development Kit (ADK)
to orchestrate Gemini-powered agents alongside our MCP tools.

Architecture Overview:
1. Gemini LLM provides the core reasoning intelligence.
2. Google ADK provides the agentic memory, tool calling, and workflow wrappers.
3. Our MCP Tools provide physical sandboxed file system capabilities.
"""

from .tools_adapter import ADKToolsAdapter

# Note: google-adk is a pseudo-SDK standard expected by the environment or an upcoming preview library.
# We mock the structure here as a robust architectural pattern.
try:
    from google_adk import Agent, Model
except ImportError:
    # Fallback mock for the hackathon environment if google_adk is not globally installed yet
    class Agent:
        def __init__(self, name, role, instructions, tools=None, model=None):
            self.name = name
            self.role = role
            self.instructions = instructions
            self.tools = tools or []
            self.model = model
            
        def run(self, input_text: str):
            return {"output": f"Mock ADK Agent [{self.name}] executed: {input_text}"}

    class Model:
        def __init__(self, model_name):
            self.model_name = model_name

# Define the shared Gemini model configuration
gemini_model = Model(model_name="gemini-2.5-flash")

# 1. Planner Agent
planner_agent = Agent(
    name="PlannerAgent",
    role="Systems Architect",
    instructions="""
    You are the Systems Architect. Analyze the user's project description and extract the core modules needed.
    Evaluate the technical complexity (Low, Medium, High).
    Return a detailed architectural summary.
    """,
    model=gemini_model
)

# 2. Task Manager Agent
task_manager_agent = Agent(
    name="TaskManagerAgent",
    role="Technical Project Manager",
    instructions="""
    You are a Technical Project Manager. Given an architectural summary, break down the project into a sequential roadmap.
    Generate a list of actionable development tasks (at least 15), including priority, estimated hours, and dependencies.
    """,
    model=gemini_model
)

# 3. Tech Advisor Agent
tech_advisor_agent = Agent(
    name="TechAdvisorAgent",
    role="Stack Consultant",
    instructions="""
    You are a Tech Stack Consultant. Based on the project requirements, recommend the best tools for:
    - Frontend
    - Backend
    - Database
    - Deployment
    Provide a solid reasoning for your choices.
    """,
    model=gemini_model
)

# 4. Code Generator Agent (Equipped with MCP Tools)
code_generator_agent = Agent(
    name="CodeGeneratorAgent",
    role="Senior Software Engineer",
    instructions="""
    You are a Senior Software Engineer. You write clean, production-ready code.
    Use your tools to physically create the project folder structure and write boilerplate code.
    Always create `backend/main.py`, `backend/requirements.txt`, and `frontend/src/App.tsx`.
    """,
    tools=[
        ADKToolsAdapter.create_project_workspace_tool,
        ADKToolsAdapter.create_folder_tool,
        ADKToolsAdapter.write_file_tool
    ],
    model=gemini_model
)

# 5. Reviewer Agent
reviewer_agent = Agent(
    name="ReviewerAgent",
    role="Security & Architecture Reviewer",
    instructions="""
    You are a strict Code Reviewer. Analyze the generated code and architecture.
    Identify Strengths, Risks, and actionable Suggestions. Focus on security and scalability.
    """,
    model=gemini_model
)

# 6. Documentation Agent (Equipped with MCP Tools)
documentation_agent = Agent(
    name="DocumentationAgent",
    role="Technical Writer",
    instructions="""
    You are a Technical Writer. Write a comprehensive README.md for the project.
    Use your write_file_tool to save the README.md to the project workspace root.
    """,
    tools=[
        ADKToolsAdapter.write_file_tool,
        ADKToolsAdapter.create_zip_export_tool
    ],
    model=gemini_model
)
