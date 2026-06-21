# Backend

## Overview

The backend is responsible for coordinating AI agents, handling user requests, and communicating with MCP tools.

It is implemented using FastAPI.

---

## Technology Stack

* Python
* FastAPI
* Google ADK
* MCP Server
* Gemini API

---

## Responsibilities

* Receive frontend requests
* Coordinate AI agents
* Execute MCP tools
* Generate software project plans
* Return results to the frontend

---

## Folder Structure

```text
backend/

agents/

planner/

reviewer/

generator/

tools/

mcp/

api/

main.py
```

---

## Run

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

```bash
source .venv/bin/activate
```

or (Windows)

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn main:app --reload
```

---

## Future Improvements

* GitHub Integration
* Jira Integration
* Docker Support
* Cloud Deployment
* Multi-Agent Collaboration
* Automated Testing
