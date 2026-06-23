from .gemini_client import GeminiClient

class TechAdvisorAgent:
    """
    Tech Advisor Agent
    
    Responsibilities:
    - Recommend technologies according to project requirements and tasks.
    - Suggest frontend, backend, database, and deployment stack.
    """

    def __init__(self):
        self.gemini = GeminiClient()

    async def recommend_stack(self, task_list: dict) -> dict:
        """
        Recommends a technology stack based on the project tasks.
        """
        fallback = {
            "frontend": ["React", "TypeScript", "Tailwind CSS"],
            "backend": ["FastAPI", "Python"],
            "database": ["PostgreSQL", "Redis"],
            "deployment": ["Docker", "Google Cloud Run"],
            "reason": "This stack provides a high-performance backend with FastAPI and a robust, type-safe frontend with React/TypeScript, ensuring scalable and maintainable development."
        }
        
        prompt = f"""
        You are a highly experienced Software Architect.
        Given the following development tasks and roadmap, recommend an appropriate and modern technology stack.
        
        Project Tasks and Roadmap:
        {task_list}
        
        Return a JSON object with:
        - "frontend": Array of strings (e.g., framework, UI library).
        - "backend": Array of strings (e.g., language, framework).
        - "database": Array of strings (e.g., SQL/NoSQL engine, caching).
        - "deployment": Array of strings (e.g., cloud provider, containerization tools).
        - "reason": A detailed paragraph explaining why this specific technology stack is the best fit for this project context.
        """
        
        return await self.gemini.generate_json(prompt, fallback)
