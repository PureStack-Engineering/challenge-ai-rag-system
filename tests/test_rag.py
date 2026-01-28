import pytest
import os
import sys
from unittest.mock import patch, MagicMock

try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass 


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from rag_system import RAGSystem
except ImportError:
    try:
        from src.rag_system import RAGSystem
    except ImportError:
        pytest.fail("❌ No se encontró la clase 'RAGSystem'.")


TEST_KNOWLEDGE_FILE = "test_knowledge.txt"
TEST_CONTENT = """
PureStack es una firma de auditoría de talento técnico.
Nuestro enfoque es Engineering Recruiting.
Validamos candidatos mediante retos de código en GitHub.
"""

@pytest.fixture
def rag_instance():
    """Fixture que prepara el entorno antes de cada test."""
    with open(TEST_KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
        f.write(TEST_CONTENT)
    
    try:
        rag = RAGSystem(knowledge_path=TEST_KNOWLEDGE_FILE)
    except Exception as e:
        pytest.fail(f"❌ Error al instanciar RAGSystem: {e}")

    yield rag

    if os.path.exists(TEST_KNOWLEDGE_FILE):
        os.remove(TEST_KNOWLEDGE_FILE)

    if os.path.exists("chroma_db"):
        import shutil
        shutil.rmtree("chroma_db", ignore_errors=True)

def test_ingestion(rag_instance):
    try:
        rag_instance.ingest()
    except Exception as e:
        pytest.fail(f"❌ La función 'ingest()' falló: {e}")
    assert True

def test_retrieval_logic(rag_instance):
    rag_instance.ingest()
    query = "¿Cómo valida PureStack?"
    
    try:
        results = rag_instance.retrieve(query, top_k=1)
    except AttributeError:
        pytest.fail("❌ Falta método 'retrieve'.")
    
    if not results:
        pytest.fail("❌ Retrieval vacío.")
        
    top_result = str(results[0])

    assert "retos" in top_result.lower() or "github" in top_result.lower(), \
        f"❌ Retrieval fallido. Recibido: {top_result}"

@patch('openai.ChatCompletion.create')
def test_generation_mocked(mock_openai, rag_instance):

    mock_response = MagicMock()
    mock_response.choices[0].message.content = "PureStack valida con retos."
    mock_openai.return_value = mock_response

    rag_instance.ingest()
    
    with patch.object(rag_instance, 'retrieve', return_value=["PureStack valida con retos."]):
        try:
            respuesta = rag_instance.answer("¿Qué hace PureStack?")
        except Exception as e:
 
            pytest.fail(f"❌ Fallo en answer(): {e}")

    assert "PureStack" in respuesta
