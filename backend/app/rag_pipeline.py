"""
Módulo de Orquestación RAG
Fase 1: Estructura del pipeline de búsqueda vectorial e inferencia
"""

class RAGPipeline:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        return (
            "Eres PoliBot Software, tutor virtual de Ingeniería de Software del Politécnico Grancolombiano. "
            "Responde basándote únicamente en el contexto proporcionado."
        )

    def retrieve_context(self, query: str, top_k: int = 3) -> list:
        """
        Recupera los k fragmentos (chunks) más relevantes desde la base de datos vectorial
        utilizando similitud de coseno.
        """
        return []

    def generate_response(self, query: str, context_chunks: list) -> str:
        """
        Combina la consulta del usuario, el System Prompt y el contexto recuperado
        para enviar el prompt final al modelo de lenguaje (LLM).
        """
        return ""
