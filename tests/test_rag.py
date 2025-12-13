import pytest
from unittest.mock import patch, MagicMock
import os
# Asumimos que el candidato estructura su código así. 
# Si el challenge tiene otra estructura, ajustamos la importación.
from src.rag_engine import RAGEngine 

# --- CONFIGURACIÓN ---
TEST_DATA_PATH = "data/test_knowledge.txt"

@pytest.fixture
def rag_system():
    """Inicializa el motor RAG antes de cada test."""
    # Aseguramos que exista el archivo de prueba
    if not os.path.exists(TEST_DATA_PATH):
        os.makedirs("data", exist_ok=True)
        with open(TEST_DATA_PATH, "w") as f:
            f.write("PureStack valida ingenieros con código real.\n")
            
    engine = RAGEngine(knowledge_base_path=TEST_DATA_PATH)
    engine.ingest() # Simulamos el proceso de lectura y vectorización
    return engine

def test_document_ingestion(rag_system):
    """Prueba 1: ¿Se han cargado los documentos en la base vectorial?"""
    # Asumiendo que usa ChromaDB o FAISS y expone un contador o colección
    assert rag_system.count_documents() > 0, "❌ El sistema no ha ingestado ningún documento."

def test_retrieval_accuracy(rag_system):
    """Prueba 2: Precisión de Recuperación (Lo más importante)."""
    query = "¿Cómo valida PureStack a los ingenieros?"
    
    # Pedimos al sistema que recupere los documentos relevantes (SIN generar respuesta aún)
    retrieved_docs = rag_system.retrieve(query, top_k=1)
    
    # Validamos que el texto recuperado contenga la palabra clave esperada
    top_result = retrieved_docs[0]
    assert "código real" in top_result or "valida" in top_result, \
        f"❌ El retrieval falló. Buscamos 'código real', obtuvimos: {top_result}"

@patch('src.rag_engine.openai.ChatCompletion.create')
def test_generation_mock(mock_openai, rag_system):
    """Prueba 3: Generación (Mockeada).
    Verificamos que el sistema construye el prompt y llama a la IA, 
    pero NO gastamos créditos ni necesitamos API Key real.
    """
    # Configuramos el mock para devolver una respuesta falsa exitosa
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "PureStack usa código real."
    mock_openai.return_value = mock_response

    response = rag_system.answer("¿Qué hace PureStack?")

    # Verificamos que la respuesta del método sea lo que devolvió el mock
    assert response == "PureStack usa código real."
    
    # Verificamos que se llamó a la API (o sea, que el código intenta conectar)
    assert mock_openai.called, "❌ El sistema no intentó llamar a la API de LLM."
