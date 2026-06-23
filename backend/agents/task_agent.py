from .gemini_client import GeminiClient

class TaskManagerAgent:
    """
    Task Manager Agent
    
    Responsibilities:
    - Break the project into development tasks.
    - Assign priorities to tasks.
    - Organize milestones/sprints.
    """

    def __init__(self):
        self.gemini = GeminiClient()

    async def generate_tasks(self, project_summary: dict) -> dict:
        """
        Breaks down the project summary into an actionable task list and roadmap.
        """
        summary_text = project_summary.get('summary', 'Project')
        modules = project_summary.get('modules', [])
        
        # Ensure we have a project-specific fallback even if no modules were returned
        if not modules:
            modules = ["Core Feature 1", "Core Feature 2", "Core Feature 3"]
            
        fallback_tasks = []
        for i, mod in enumerate(modules):
            fallback_tasks.append({
                "title": f"Implement {mod} Backend",
                "description": f"Develop the core functionalities, database models, and API endpoints for {mod}.",
                "priority": "High" if i < 3 else "Medium",
                "status": "Todo",
                "estimated_hours": 20,
                "dependencies": []
            })
            fallback_tasks.append({
                "title": f"Design {mod} UI",
                "description": f"Create wireframes and React components for the {mod} interface.",
                "priority": "Medium",
                "status": "Todo",
                "estimated_hours": 15,
                "dependencies": [f"Implement {mod} Backend"]
            })

        # Ensure we have at least 15 tasks
        while len(fallback_tasks) < 15:
            idx = len(fallback_tasks)
            fallback_tasks.append({
                "title": f"Additional Project Task {idx}",
                "description": f"Refine features and optimize queries for Task {idx}.",
                "priority": "Low",
                "status": "Todo",
                "estimated_hours": 5,
                "dependencies": []
            })

        fallback = {
            "roadmap": [
                f"Phase 1: Architecture & {modules[0] if modules else 'Core'} Planning",
                f"Phase 2: Authentication & Secure Setup",
                f"Phase 3: Developing {modules[0] if modules else 'Backend'}",
                f"Phase 4: Developing {modules[1] if len(modules) > 1 else 'Frontend'}",
                f"Phase 5: User Interface Integration",
                f"Phase 6: Quality Assurance & Testing",
                f"Phase 7: Production Deployment"
            ],
            "tasks": fallback_tasks[:15]
        }
        
        prompt = f"""
        You are an expert Agile Task Manager and Scrum Master.
        Given the following project summary and its domain-specific modules, break down the project into a highly detailed roadmap and actionable development tasks.
        
        Project Context:
        {project_summary}
        
        Return a JSON object with:
        - "roadmap": An array of strings containing 6 to 8 project-specific phases representing the high-level roadmap of the project lifecycle. Instead of generic phases, integrate the module names and project domain into the phase titles.
        - "tasks": An array of objects representing at least 15 highly detailed, project-specific development tasks. Each object must contain exactly:
            - "title": A concise, descriptive string of the task.
            - "description": A 1-2 sentence detailed explanation of the task, referencing specific domain features.
            - "priority": A string ("High", "Medium", or "Low").
            - "status": Always the string "Todo".
            - "estimated_hours": An integer representing the estimated development time in hours.
            - "dependencies": An array of strings containing the titles of tasks that must be completed before this one.
        """
        
        return await self.gemini.generate_json(prompt, fallback)
