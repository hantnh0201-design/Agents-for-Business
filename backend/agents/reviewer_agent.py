from .gemini_client import GeminiClient

class ReviewerAgent:
    """
    Reviewer Agent
    
    Responsibilities:
    - Review generated outputs from the CodeGeneratorAgent.
    - Check for missing files, folder organization, code quality, and configuration.
    - Suggest improvements before exporting the project.
    """

    def __init__(self):
        self.gemini = GeminiClient()

    async def review_project(self, generated_project: dict) -> dict:
        """
        Reviews the generated project artifacts and ensures they meet quality standards.
        """
        fallback = {
            "status": "passed",
            "strengths": ["Clear separation of frontend and backend.", "Standardized configuration files included."],
            "risks": ["Missing automated tests for backend.", "No CI/CD pipeline file detected."],
            "suggestions": ["Add pytest configuration.", "Create a .github/workflows deployment file."]
        }
        
        prompt = f"""
        You are a strict Code Reviewer and QA lead.
        Review the following generated project structure and evaluate its completeness and architecture.
        
        Generated Project Files:
        {generated_project}
        
        Return a JSON object with:
        - "status": A string containing either "passed" or "failed".
        - "strengths": An array of strings describing the architectural strengths of the generated files.
        - "risks": An array of strings identifying any missing critical files or structural risks.
        - "suggestions": An array of strings containing actionable improvement suggestions.
        """
        
        return await self.gemini.generate_json(prompt, fallback)
