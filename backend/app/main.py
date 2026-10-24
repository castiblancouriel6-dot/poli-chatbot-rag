```python
"""
API REST Backend - Chatbot Educativo RAG
Institución Universitaria Politécnico Grancolombiano
Fase 1: Estructura base de la aplicación API REST
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="PoliBot Software API",
    description="API REST para el pipeline de consulta y generación RAG del Chatbot de Ingeniería de Software",
    version="0.1.0"
)

class QueryRequest(BaseModel):
    user_id: str
    query: str
    session_id: Optional[str] = None

class QueryResponse(BaseModel):
    response: str
    sources: list[str]
    session_id: str

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "PoliBot Software RAG API",
        "version": "0.1.0"
    }

@app.post("/api/v1/chat", response_model=QueryResponse)
def handle_chat_query(request: QueryRequest):
    """
    Endpoint principal para recibir consultas de los estudiantes
    e iterar con el pipeline RAG.
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="La consulta no puede estar vacía.")
    
    return QueryResponse(
        response="[PoliBot Software]: Módulo de respuesta en proceso de integración con la base de datos vectorial.",
        sources=["Syllabus_Ingenieria_Software.pdf"],
        session_id=request.session_id or "session_default"
    )
