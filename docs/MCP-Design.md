# MCP Server Design

# 1. Overview

The MCP Server is an important component of DevPilot AI. It provides tools that allow AI agents to interact with the project workspace.

Instead of only generating text, agents can use MCP tools to perform actions such as creating folders, writing files, reading files, listing directories, and generating documentation.

---

# 2. Purpose of MCP Server

The purpose of the MCP Server is to give AI agents controlled access to external tools.

In DevPilot AI, MCP tools help agents:

* Create project folders
* Generate starter files
* Read existing files
* Write source code
* Generate README documentation
* Execute safe commands
* Organize project outputs

---

# 3. MCP Server Role in Architecture

```text
User
  ↓
Frontend
  ↓
Backend
  ↓
AI Agent System
  ↓
MCP Server
  ↓
Project Workspace
```

The AI Agent System calls MCP tools when it needs to perform a real action inside the project workspace.

---

# 4. Planned MCP Tools

## 4.1 Create Folder Tool

Tool name:

```text
create_folder
```

Purpose:

Create a new folder inside the project workspace.

Example:

```text
create_folder("frontend")
create_folder("backend")
create_folder("docs")
```

---

## 4.2 Write File Tool

Tool name:

```text
write_file
```

Purpose:

Write generated content into a file.

Example:

```text
write_file("README.md", content)
write_file("backend/main.py", content)
write_file("frontend/src/App.tsx", content)
```

---

## 4.3 Read File Tool

Tool name:

```text
read_file
```

Purpose:

Read existing file content for review or modification.

Example:

```text
read_file("README.md")
```

---

## 4.4 List Directory Tool

Tool name:

```text
list_directory
```

Purpose:

List files and folders inside the workspace.

Example:

```text
list_directory(".")
list_directory("frontend")
```

---

## 4.5 Generate README Tool

Tool name:

```text
generate_readme
```

Purpose:

Generate README documentation based on project metadata.

Output:

* Project overview
* Features
* Tech stack
* Installation
* Usage
* Deployment guide

---

## 4.6 Safe Command Tool

Tool name:

```text
run_safe_command
```

Purpose:

Run predefined safe terminal commands.

Allowed commands:

```text
npm install
npm run build
pip install -r requirements.txt
python -m pytest
```

Blocked commands:

```text
rm -rf
del /s
format
shutdown
curl unknown-url
```

This prevents dangerous operations.

---

# 5. Workspace Restriction

The MCP Server only works inside the generated project workspace.

Example workspace:

```text
generated_projects/
```

Agents are not allowed to access files outside this folder.

This improves security and prevents accidental modification of sensitive files.

---

# 6. Tool Input and Output Design

## create_folder

Input:

```json
{
  "path": "backend"
}
```

Output:

```json
{
  "status": "success",
  "message": "Folder created successfully."
}
```

---

## write_file

Input:

```json
{
  "path": "README.md",
  "content": "# DevPilot AI Generated Project"
}
```

Output:

```json
{
  "status": "success",
  "message": "File written successfully."
}
```

---

## read_file

Input:

```json
{
  "path": "README.md"
}
```

Output:

```json
{
  "status": "success",
  "content": "# DevPilot AI Generated Project"
}
```

---

## list_directory

Input:

```json
{
  "path": "."
}
```

Output:

```json
{
  "status": "success",
  "items": [
    "frontend",
    "backend",
    "README.md"
  ]
}
```

---

## run_safe_command

Input:

```json
{
  "command": "npm run build"
}
```

Output:

```json
{
  "status": "success",
  "output": "Build completed successfully."
}
```

---

# 7. Security Design

The MCP Server follows these security principles:

* Only access files inside the workspace.
* Reject absolute paths.
* Reject paths containing `..`.
* Allow only predefined safe commands.
* Never expose API keys or environment variables.
* Log all tool calls.
* Validate all inputs before execution.

---

# 8. Example MCP Workflow

Example: User asks to generate a Flower Shop Website.

```text
1. Code Generator Agent requests project folder creation.
2. MCP Server calls create_folder("frontend").
3. MCP Server calls create_folder("backend").
4. MCP Server calls write_file("README.md", content).
5. MCP Server calls write_file("backend/main.py", backend_code).
6. MCP Server calls write_file("frontend/src/App.tsx", frontend_code).
7. Reviewer Agent calls list_directory(".").
8. Reviewer Agent checks generated files.
9. Documentation Agent updates README.md.
```

---

# 9. Why MCP Is Important

MCP is important because it allows AI agents to use tools in a structured and secure way.

Without MCP, the agent can only generate text.

With MCP, the agent can:

* Create real project files
* Modify generated outputs
* Review project structure
* Prepare deliverable artifacts
* Support real-world developer workflows

---

# 10. Future MCP Tools

Future versions may include:

* GitHub tool
* Jira tool
* Google Drive tool
* Database schema generator
* Dockerfile generator
* CI/CD pipeline generator
* Cloud deployment helper

---

# 11. Summary

The MCP Server extends DevPilot AI by giving agents controlled access to project tools. It allows the system to move from simple AI-generated responses to practical software project generation.

This design supports automation, security, and real-world usability, which are important criteria for the AI Agents capstone project.
