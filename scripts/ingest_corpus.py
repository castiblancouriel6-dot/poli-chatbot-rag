"""
Script de Procesamiento e Ingesta del Corpus Académico
Fase 1: Definición de parámetros de fragmentación (Chunking)
"""

CHUNK_SIZE = 500      # Tamaño del bloque en tokens
CHUNK_OVERLAP = 50    # Solapamiento del 10%

def load_documents(directory_path: str) -> list:
    """
    Lee y extrae texto de archivos del corpus académico.
    """
    print(f"Cargando documentos desde {directory_path}...")
    return []

def split_text_into_chunks(documents: list) -> list:
    """
    Divide los textos en fragmentos de 500 tokens con 10% de solapamiento.
    """
    print(f"Dividiendo textos en chunks (Tamaño: {CHUNK_SIZE}, Solapamiento: {CHUNK_OVERLAP})...")
    return []

if __name__ == "__main__":
    print("=== PROCESAMIENTO INICIAL DEL CORPUS ACADÉMICO (FASE 1) ===")
    docs = load_documents("./corpus")
    text_chunks = split_text_into_chunks(docs)
    print("Estructura de ingesta preparada para el Sprint 2.")
