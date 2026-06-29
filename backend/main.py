import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
import json

from backend.agent import stream_chat_response, fetch_live_github_projects

# Initialize FastAPI
app = FastAPI(
    title="Anjani Kushwaha's Portfolio AI Agent Backend",
    description="FastAPI Backend powering the RAG agent and GitHub sync tool",
    version="1.0.0"
)

# Configure CORS so the static frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local portfolio execution
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatPayload(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

@app.get("/health")
def health_check():
    """Verify that backend is running."""
    return {"status": "healthy", "groq_api_key_configured": bool(os.getenv("GROQ_API_KEY"))}

@app.get("/api/projects")
def get_projects():
    """API endpoint to get live github projects of Anjani."""
    projects = fetch_live_github_projects()
    return {"projects": projects}

@app.post("/chat")
def chat_endpoint(payload: ChatPayload):
    """
    POST /chat endpoint that streams responses using Server-Sent Events (SSE).
    """
    history_list = []
    if payload.history:
        for msg in payload.history:
            history_list.append({
                "role": msg.role,
                "content": msg.content
            })

    def event_generator():
        try:
            for chunk in stream_chat_response(payload.message, history_list):
                # Send SSE formatted chunk data
                yield f"data: {json.dumps({'text': chunk})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
        # Terminate connection
        yield "data: [DONE]\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"Starting backend server on port {port}...")
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=True)
