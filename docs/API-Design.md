# API Design

## Overview

The backend is built with FastAPI and exposes RESTful APIs for communication between the frontend and the AI Agent system.

Base URL:

```text
http://localhost:8000
```

---

# Endpoints

## Health Check

**GET /health**

Description:

Returns the backend status.

Example Response

```json
{
    "status": "healthy"
}
```

---

## Generate Project

**POST /generate**

Description:

Generate a complete software project plan from the user's description.

Request

```json
{
    "project_name": "Flower Shop Website",
    "description": "Build an online flower shop with admin dashboard.",
    "tech_stack": "React, FastAPI, SQLite"
}
```

Response

```json
{
    "project_id": "12345",
    "status": "success",
    "summary": "Online Flower Shop",
    "roadmap": [
        "Requirement Analysis",
        "Database Design",
        "Frontend Development",
        "Backend Development",
        "Testing",
        "Deployment"
    ]
}
```

---

## Get Project

**GET /projects/{project_id}**

Description:

Retrieve project information.

Response

```json
{
    "project_id": "12345",
    "name": "Flower Shop Website",
    "status": "Completed"
}
```

---

## Get Generated Files

**GET /projects/{project_id}/files**

Description:

Returns generated files.

Example

```json
{
    "files": [
        "README.md",
        "frontend/src/App.tsx",
        "backend/main.py"
    ]
}
```

---

## Export Project

**POST /projects/{project_id}/export**

Description:

Export the generated project as a ZIP package.

Response

```json
{
    "download_url": "/downloads/project.zip"
}
```

---

# Error Response

```json
{
    "status": "error",
    "message": "Invalid request."
}
```

---

# Future APIs

* POST /review
* POST /generate-code
* POST /generate-readme
* POST /deploy
* POST /chat
