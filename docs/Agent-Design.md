# DevPilot AI Agent Design

DevPilot AI implements a dual-track architectural approach for its multi-agent system.

## 1. Production Track (Gemini REST API)
Located in `backend/agents/`, this is the stable, production-ready workflow. It leverages direct REST calls to Google Gemini, orchestrating a sequence of highly specialized prompting phases.

Agents:
- PlannerAgent
- TaskManagerAgent
- TechAdvisorAgent
- CodeGeneratorAgent (direct tool invocation)
- ReviewerAgent
- DocumentationAgent

## 2. Experimental Google ADK Track
Located in `backend/adk_agents/`, this track adopts the highly-structured **Google Agent Development Kit (ADK)**. 

### ADK Workflow Integration
Instead of raw strings and manual REST loops, the ADK track encapsulates logic into formal `Agent` and `Model` primitives.

#### The `tools_adapter.py`
The most critical piece of the ADK track is the `ADKToolsAdapter`. It takes our raw, secure MCP filesystem functions (like `create_project_workspace`) and wraps them into a format directly consumable by the `google-adk` `Agent.tools` array. 

This enables the ADK-driven `CodeGeneratorAgent` and `DocumentationAgent` to inherently "understand" and execute physical filesystem writes while remaining securely sandboxed.

### Unified Capabilities
Regardless of which track is active, both workflows:
1. Emulate the exact same 6 roles (Architect, PM, Consultant, Engineer, Reviewer, Tech Writer).
2. Share the same `gemini-2.5-flash` cognitive engine.
3. Access the identical, sandboxed Model Context Protocol (MCP) toolset.
