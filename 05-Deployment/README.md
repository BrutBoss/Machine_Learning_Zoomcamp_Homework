# 🚀 FastAPI + uv + Docker

A lightweight FastAPI service using **uv** for dependency management and containerized with Docker.  
Runs seamlessly with `uvicorn` on port **8000**.

**Quick start:**
```bash
docker build -t fastapi-uv-app .
docker run -p 8000:8000 fastapi-uv-app
