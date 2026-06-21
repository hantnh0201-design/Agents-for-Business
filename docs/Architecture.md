# DevPilot AI - System Architecture

## 1. Overview

DevPilot AI is an intelligent AI Project Manager Agent designed to help developers transform software ideas into structured development plans. Instead of simply answering questions like a chatbot, the system analyzes project requirements, generates development tasks, creates an implementation roadmap, produces starter project structures, reviews generated outputs, and prepares project documentation.

The system follows a multi-agent architecture where specialized AI agents collaborate to complete different stages of software project planning and initialization.

---

# 2. Project Goal

The goal of DevPilot AI is to reduce the time developers spend planning new software projects.

The agent automatically performs tasks such as:

* Analyze project requirements
* Generate development roadmap
* Break down projects into actionable tasks
* Suggest appropriate technology stack
* Create project folder structure
* Generate starter code
* Review generated code
* Generate README documentation

---

# 3. Overall System Architecture

The system consists of four major layers.

## User Layer

The user provides a project idea using a web interface.

Example:

"I want to build a Flower Shop Website with product management and online ordering."

---

## Frontend Layer

Technology:

* React
* TypeScript
* Tailwind CSS

Responsibilities:

* Accept user input
* Display generated roadmap
* Display generated tasks
* Show AI Agent execution logs
* Preview generated files
* Download generated project

---

## Backend Layer

Technology:

* FastAPI

Responsibilities:

* Receive requests from the frontend
* Communicate with the AI Agent System
* Manage project data
* Return generated results

Main API endpoints:

* POST /generate
* GET /projects/{id}
* GET /health

---

## AI Agent Layer

The AI Agent System is responsible for reasoning and decision making.

It consists of multiple specialized agents.

### Main Orchestrator Agent

Responsibilities:

* Receive user request
* Coordinate all agents
* Manage execution workflow

---

### Planner Agent

Responsibilities:

* Analyze user requirements
* Identify project objectives
* Suggest technology stack

Output:

* Project summary
* Development roadmap

---

### Task Manager Agent

Responsibilities:

* Break the project into development tasks
* Assign priorities
* Organize tasks into milestones

Output:

* Task list
* Sprint roadmap

---

### Code Generator Agent

Responsibilities:

* Generate starter project structure
* Generate initial source code
* Create configuration files

Output:

* Frontend structure
* Backend structure
* Configuration files

---

### Reviewer Agent

Responsibilities:

* Review generated code
* Detect missing files
* Check project consistency
* Suggest improvements

Output:

* Review report

---

### Documentation Agent

Responsibilities:

* Generate README
* Generate installation guide
* Generate deployment instructions

Output:

* README.md
* Documentation

---

# 4. MCP Server

The MCP Server provides tools that allow AI agents to perform actions instead of only generating text.

Available tools include:

* Read file
* Write file
* Create folder
* List directory
* Generate README
* Execute safe terminal commands

These tools enable the agents to create and organize a real software project.

---

# 5. Workflow

The workflow of DevPilot AI is as follows:

1. User enters a project description.
2. Frontend sends the request to the backend.
3. Backend forwards the request to the Main Orchestrator Agent.
4. Planner Agent analyzes the project requirements.
5. Task Manager Agent generates a task list and roadmap.
6. Code Generator Agent creates the starter project.
7. Reviewer Agent validates the generated output.
8. Documentation Agent generates project documentation.
9. Backend returns the final result.
10. Frontend displays the generated roadmap, tasks, code structure, and documentation.

---

# 6. Input Example

```json
{
  "project_name": "Flower Shop Website",
  "description": "Build an online flower shop with product management, shopping cart, payment and admin dashboard.",
  "tech_stack": "React, FastAPI, SQLite"
}
```

---

# 7. Output Example

```json
{
  "summary": "Online flower shop",
  "roadmap": [
    "Requirement Analysis",
    "Database Design",
    "Frontend Development",
    "Backend Development",
    "Testing",
    "Deployment"
  ],
  "tasks": [
    {
      "title": "Create Product Page",
      "priority": "High",
      "status": "Todo"
    },
    {
      "title": "Build Shopping Cart",
      "priority": "High",
      "status": "Todo"
    }
  ],
  "generated_files": [
    "README.md",
    "frontend/src/App.tsx",
    "backend/main.py"
  ]
}
```

---

# 8. Security Considerations

To ensure security, the system follows these principles:

* API keys are stored in environment variables (.env).
* Sensitive information is never hardcoded.
* MCP tools only operate inside the project workspace.
* Only predefined safe terminal commands are allowed.
* User input is validated before processing.

---

# 9. Deployment Plan

Frontend:

* React
* Deploy to Vercel

Backend:

* FastAPI
* Deploy to Google Cloud Run

Repository:

* GitHub

The GitHub repository contains installation instructions and setup documentation for local execution.

---

# 10. Future Improvements

Future versions of DevPilot AI may include:

* GitHub integration
* Jira integration
* Automatic issue creation
* Team collaboration support
* Multi-language project generation
* CI/CD pipeline generation
* Docker and Kubernetes deployment support
* Cloud infrastructure recommendation

---

# 11. Expected Benefits

DevPilot AI provides the following benefits:

* Reduce project planning time.
* Improve software development efficiency.
* Help beginners start projects more easily.
* Generate consistent project structures.
* Produce documentation automatically.
* Improve code quality through automated review.

This architecture provides a scalable foundation for building intelligent AI agents capable of assisting developers throughout the software development lifecycle.
