# Chatbot Educativo con Arquitectura RAG - Ingeniería de Software

Este repositorio contiene la arquitectura, especificaciones de diseño y estructura base del chatbot educativo desarrollado para el apoyo pedagógico de los estudiantes de la carrera de Ingeniería de Software de la Institución Universitaria Politécnico Grancolombiano.

## Estructura del Proyecto

```text
poli-chatbot-rag/
├── README.md
├── .gitignore
├── docs/
│   ├── arquitectura_rag.jpg
│   ├── flujo_conversacional.jpg
│   └── system_prompt_spec.md
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag_pipeline.py
│   │   ├── vector_store.py
│   │   └── prompts.py
│   └── requirements.txt
├── scripts/
│   ├── ingest_corpus.py
│   └── generate_embeddings.py
└── frontend/
    └── README.md
