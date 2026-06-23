from .gemini_client import GeminiClient

class PlannerAgent:
    """
    Planner Agent
    
    Responsibilities:
    - Understand project requirements from the user.
    - Identify project goals.
    - Determine project scope.
    - Estimate development complexity.
    """

    def __init__(self):
        self.gemini = GeminiClient()

    async def analyze_project(self, user_request: dict) -> dict:
        """
        Analyzes the project description to produce a comprehensive summary.
        """
        name = user_request.get("project_name", "Unknown Project")
        desc = user_request.get("description", "No description provided.")
        tech = user_request.get("tech_stack", "No specific tech stack.")
        
        fallback = {
            "summary": f"Comprehensive Platform for {name}",
            "modules": [
                f"{name} User Management",
                f"{name} Core Features Dashboard",
                f"{name} Advanced Reporting",
                f"{name} Settings and Configuration",
                f"{name} Billing and Invoicing"
            ],
            "complexity": "Medium"
        }
        
        prompt = f"""
        You are an expert AI software planner. 
        Analyze the following project request and return a JSON object containing highly domain-specific and project-specific details.
        
        Project Name: {name}
        Description: {desc}
        Requested Tech Stack: {tech}

        Return a JSON object with:
        - "summary": A detailed 2-3 sentence description of the project goals and business value.
        - "modules": An array of strings representing the main functional modules to be built. You MUST make these extremely domain-specific. 
            For example, if it's a Hospital Management System, modules should include "Patient Management", "Doctor Management", "Appointment Scheduling", "Pharmacy Management", "Billing Management", "Laboratory Management", "Reporting Dashboard", "Authentication and Authorization".
            DO NOT use generic module names like "Core Application Logic", "Data Management & Storage", or "API Integration & Webhooks". Generate at least 5-8 highly tailored modules.
        - "complexity": A string ("Low", "Medium", "High") estimating the overall project development complexity based on the description.
        """
        
        return await self.gemini.generate_json(prompt, fallback)
