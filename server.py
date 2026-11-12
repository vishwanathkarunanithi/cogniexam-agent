"""
FastAPI Server for CogniExam Multi-Agent System.
Serves the React Native Web frontend and provides REST endpoints.
"""

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router

app = FastAPI(
    title="CogniExam AI Agent Platform",
    description="Bloom's Taxonomy Question Paper Auditor & Answer Key Synthesizer",
    version="2.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API endpoints
app.include_router(api_router)

# Mount frontend directory
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.exists(frontend_dir):
    @app.get("/")
    def serve_react_app():
        return FileResponse(os.path.join(frontend_dir, "index.html"))

    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"[*] Starting CogniExam Server on http://localhost:{port}")
    uvicorn.run("server.py:app", host="0.0.0.0", port=port, reload=False)

