# 🚀 DevPilot AI
**Intelligent Auto-Scaffolding & Architecture Agent**

DevPilot AI is an advanced multi-agent system powered by **Google Gemini** that automates the software development lifecycle. By analyzing a simple text description of a project, it automatically architects a domain-specific system, generates actionable tasks, and physically scaffolds the project files directly to your machine using **MCP (Model Context Protocol)** tools.

---

## 🛑 Problem Statement
Setting up a new project involves tedious, repetitive tasks: defining architecture, creating folder structures, initializing configurations, writing starter code, and breaking down the project into tickets. This manual scaffolding wastes valuable development time and often leads to inconsistent architectures, especially in fast-paced environments like hackathons or startup incubation.

## 💡 Solution
DevPilot AI automates the entire "0 to 1" process. By leveraging a specialized **Multi-agent system** powered by the latest **Google Gemini** models, it intelligently plans the architecture, generates a full roadmap, reviews code security, and physically writes the starter application to your disk in seconds. 

Built with the assistance of **Antigravity** for development, DevPilot ensures you can focus on building features rather than configuring boilerplates.

---

## ✨ Key Features
- **Intelligent Planning**: Generates highly domain-specific modules and architecture.
- **Automated Roadmap**: Creates detailed development phases and actionable tasks with estimated hours.
- **Physical File Scaffolding**: Uses **MCP Tools** to physically write the project structure and boilerplate code to disk.
- **Expert Code Review**: Built-in agentic review process that highlights architectural strengths, risks, and suggestions.
- **Beautiful Glassmorphic Dashboard**: A premium, dark-mode web interface built with React + TypeScript.
- **Zip Export**: Automatically bundles generated projects into downloadable zip archives.

---

## 🧠 System Architecture

The system is split into two main components:
1. **Frontend**: A sleek React + TypeScript + Vite dashboard designed for hackathons.
2. **Backend**: A robust FastAPI orchestrator that coordinates a pipeline of specialized AI agents.

### Multi-Agent Workflow
The `MainOrchestratorAgent` sequentially coordinates the following specialized agents:
1. **PlannerAgent**: Extracts core domain modules and evaluates project complexity.
2. **TaskManagerAgent**: Generates a detailed roadmap and 15+ actionable development tasks.
3. **TechAdvisorAgent**: Recommends the optimal frontend, backend, database, and deployment stack.
4. **CodeGeneratorAgent**: Uses **MCP Tools** to create the workspace folder and scaffold physical code files (`App.tsx`, `main.py`, etc.).
5. **ReviewerAgent**: Analyzes the generated code and provides a comprehensive security and architectural review.
6. **DocumentationAgent**: Uses **MCP Tools** to generate a beautifully formatted `README.md` for the spawned project.

### MCP Tools (Model Context Protocol)
DevPilot AI utilizes MCP to bridge the gap between AI generation and physical file system execution. It uses secure, path-validated tools:
- `create_project_workspace(project_id)`
- `create_folder(project_id, folder_path)`
- `write_file(project_id, file_path, content)`
- `create_zip_export(project_id)`

---

## 🛠️ Tech Stack
- **AI Core**: Google Gemini (`gemini-2.5-flash`)
- **Backend**: Python, FastAPI, Uvicorn, python-dotenv
- **Frontend**: React, TypeScript, Vite, Vanilla CSS (Glassmorphism), react-markdown
- **Architecture**: Multi-Agent Orchestration, Model Context Protocol (MCP)
- **Development Partner**: Antigravity

---

## 🚀 Setup Instructions

### Environment Variables
Before running the application, you must configure your Google Gemini API key.
Create a `.env` file inside the `backend/` directory:
```env
# backend/.env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### Backend Setup
```bash
cd backend

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows:
.\.venv\Scripts\Activate.ps1
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --reload
```
The backend will run on `http://127.0.0.1:8000`.

### Frontend Setup
Open a new terminal window:
```bash
cd frontend

# Install dependencies
npm install

# Start the Vite development server
npm run dev
```
The frontend dashboard will be available at `http://localhost:5173`.

---

## 🔌 API Usage
You can trigger the multi-agent generation directly via the REST API.

**POST** `http://127.0.0.1:8000/generate`
```json
{
  "project_name": "Hospital Management System",
  "description": "A comprehensive portal for managing patients, doctor schedules, and billing.",
  "tech_stack": "React, Node, PostgreSQL"
}
```

---

## 📸 Screenshots
*(Insert screenshots of the Glassmorphic Dashboard, Roadmap Grid, and Generated Files view here)*

## 🎥 Demo Video
*(Insert link to YouTube/Loom demo video here)*

---

## 🔒 Security Notes
- **Sandboxed Execution**: All MCP tool file operations are strictly jailed to the `backend/generated_projects/{project_id}` directory.
- **Path Traversal Protection**: Absolute paths and directory traversal sequences (`..`) are heavily sanitized and blocked by the MCP wrapper.
- **API Key Safety**: The Gemini API key is loaded strictly through absolute-path environment variables and is never hardcoded or exposed to the client.

---

## 🔮 Future Improvements
- **Interactive Kanban**: Evolve the static task grid into an interactive Kanban board with drag-and-drop state persistence.
- **Agent Loops**: Allow the `ReviewerAgent` to pass feedback back to the `CodeGeneratorAgent` for auto-correction loops.
- **Live Preview**: Mount a dynamic iframe to preview the generated HTML/JS code inside the dashboard.
- **Git Integration**: Push the scaffolded workspace directly to a new GitHub repository automatically.