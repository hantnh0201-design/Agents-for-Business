# Google ADK Integration

## Why ADK is Used
The **Google Agent Development Kit (ADK)** introduces a formalized, structured layer for developing intelligent agents. While our stable FastAPI workflow successfully orchestrates raw Gemini endpoints manually, the ADK standardizes agent memory, tool delegation, and cognitive reasoning loops under a unified framework. This experimental track allows us to demonstrate state-of-the-art agent engineering practices.

## How ADK Agents Map to Existing Agents
Our ADK implementation perfectly mirrors the existing 6-agent sequential pipeline:
1. `PlannerAgent` (Systems Architect)
2. `TaskManagerAgent` (Technical Project Manager)
3. `TechAdvisorAgent` (Stack Consultant)
4. `CodeGeneratorAgent` (Senior Software Engineer)
5. `ReviewerAgent` (Security Reviewer)
6. `DocumentationAgent` (Technical Writer)

## How ADK Connects with Gemini
The Google ADK abstracts the underlying LLM via the `Model` primitive. We initialize a shared `gemini-2.5-flash` model object and bind it directly to the `model=` parameter of each ADK Agent, instantly injecting Gemini's reasoning capabilities into the structured agent loop.

## How ADK Connects with MCP Tools
To bridge the gap between abstract agent logic and physical file operations, we built `tools_adapter.py`. This layer encapsulates our secure, sandboxed Model Context Protocol (MCP) file system scripts into callable `Tool` objects that the ADK `tools=[]` array can consume.

## Why the Existing FastAPI Workflow is Kept Stable
The ADK track was intentionally built in parallel (under `backend/adk_agents/`) without replacing the `backend/agents/` code. This guarantees 100% stability for the hackathon `/generate` endpoint, ensuring the core React dashboard never experiences downtime while allowing us to experiment with ADK capabilities under the hood.
