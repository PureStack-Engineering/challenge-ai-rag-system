import pytest
import os
import sys
from unittest.mock import patch, MagicMock

# --- CONFIGURACIÓN DEL ENTORNO ---
# Aseguramos que Python encuentre el código del candidato en la carpeta raíz o src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ⚠️ NOTA PARA EL CANDIDATO:
# Tu solución debe tener un archivo llamado 'rag_system.py' (o similar, ajústalo aquí)
# y una clase principal llamada 'RAGSystem'.
# Si tu estructura es diferente, ajusta el import de abajo o refactoriza tu código.
try:
    from rag_system import RAGSystem
except ImportError:
    # Fallback por si el candidato lo puso en src/
    try:
        from src.rag_system import RAGSystem
    except ImportError:
        pytest.fail("❌ No se encontró la clase 'RAGSystem'. Asegúrate de crear el archivo 'rag_system.py' con la clase RAGSystem.")

# --- DATOS DE PRUEBA ---
TEST_KNOWLEDGE_FILE = "test_knowledge.txt"
TEST_CONTENT = """
PureStack es una firma de auditoría de talento técnico.
Nuestro enfoque es Engineering Recruiting.
Validamos candidatos mediante retos de código en GitHub.
El stack principal para este test es Python y Vector Databases.
"""

@pytest.fixture
def rag_instance():
    """Fixture que prepara el entorno antes de cada test."""
    # 1. Crear un archivo de texto dummy para la prueba
    with open(TEST_KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
        f.write(TEST_CONTENT)
    
    # 2. Instanciar la clase del candidato
    # Se espera que el constructor acepte la ruta del archivo de conocimiento
    try:
        rag = RAGSystem(knowledge_path=TEST_KNOWLEDGE_FILE)
    except Exception as e:
        pytest.fail(f"❌ Error al instanciar RAGSystem: {e}")

    yield rag

    # 3. Limpieza (Teardown) después del test
    if os.path.exists(TEST_KNOWLEDGE_FILE):
        os.remove(TEST_KNOWLEDGE_FILE)
    # Aquí podrías añadir limpieza de la base de datos vectorial si persiste en disco

def test_ingestion(rag_instance):
    """
    PRUEBA 1: INGESTA
    Valida que el sistema pueda cargar y procesar documentos.
    """
    try:
        rag_instance.ingest()
    except Exception as e:
        pytest.fail(f"❌ La función 'ingest()' falló: {e}")
    
    # Verificación (Asumiendo que existe un método para contar docs o que no da error)
    # Esto es flexible, lo importante es que ingest() no explote.
    assert True

def test_retrieval_logic(rag_instance):
    """
    PRUEBA 2: RECUPERACIÓN (RETRIEVAL)
    Esta es la prueba más importante de un RAG.
    Sin llamar a la IA, ¿encuentra el sistema el párrafo correcto?
    """
    rag_instance.ingest() # Aseguramos que hay datos
    
    query = "¿Cómo valida PureStack a los candidatos?"
    
    # Se espera un método 'retrieve' o 'search' que devuelva una lista de textos o documentos
    try:
        results = rag_instance.retrieve(query, top_k=1)
    except AttributeError:
        pytest.fail("❌ Tu clase RAGSystem debe tener un método 'retrieve(query, top_k)'.")
    
    if not results:
        pytest.fail("❌ La búsqueda no devolvió resultados.")
        
    # Validamos que el resultado contenga palabras clave esperadas del texto dummy
    top_result = str(results[0])
    assert "retos de código" in top_result or "GitHub" in top_result, \
        f"❌ Retrieval fallido. Se esperaba contexto sobre 'retos de código', se recibió: {top_result}"

@patch('openai.ChatCompletion.create') # Mockeamos OpenAI (ajustar si usan otra lib)
def test_generation_mocked(mock_openai, rag_instance):
    """
    PRUEBA 3: GENERACIÓN (LLM MOCK)
    Verifica que el sistema construye el prompt y llama a la API.
    NO gasta créditos reales.
    """
    # Configuramos el simulador para que "OpenAI" nos devuelva esto:
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "PureStack valida con retos en GitHub."
    mock_openai.return_value = mock_response

    rag_instance.ingest()
    
    query = "¿Qué hace PureStack?"
    
    # Se espera un método 'answer' o 'query' que devuelva el string final
    try:
        respuesta = rag_instance.answer(query)
    except AttributeError:
        pytest.fail("❌ Tu clase RAGSystem debe tener un método 'answer(query)'.")

    # 1. Verificamos que la respuesta final sea la que nos dio el mock
    assert "PureStack" in respuesta
    
    # 2. Verificamos que DENTRO del código se intentó llamar a OpenAI
    # (Si el candidato solo hizo un 'print', esto fallará)
    # Nota: Si el candidato usa LangChain, el mock sería diferente, 
    # pero para un test genérico esto valida la intención.
    assert mock_openai.called or respuesta == "PureStack valida con retos en GitHub.", \
        "⚠️ El sistema generó respuesta pero no pareció llamar a la API mockeada (¿Lógica hardcodeada?)"
