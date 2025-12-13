import os
# Puedes importar aquí las librerías que necesites (LangChain, Chroma, OpenAI, etc.)

class RAGSystem:
    """
    Clase principal para el sistema RAG de PureStack.
    El candidato debe completar los métodos ingest, retrieve y answer.
    """

    def __init__(self, knowledge_path):
        """
        Inicializa el sistema.
        :param knowledge_path: Ruta al archivo de texto con el conocimiento base.
        """
        self.knowledge_path = knowledge_path
        # TODO: Inicializa aquí tu base de datos vectorial y tus embeddings
        pass

    def ingest(self):
        """
        Fase 1: Ingesta
        Debe cargar el archivo de texto, dividirlo en chunks y guardarlo en la vector store.
        """
        # TODO: Implementar lógica de ingesta
        raise NotImplementedError("Debes implementar el método ingest().")

    def retrieve(self, query, top_k=1):
        """
        Fase 2: Recuperación
        Debe buscar los documentos más relevantes para la query.
        :return: Lista de strings con el contenido de los documentos recuperados.
        """
        # TODO: Implementar lógica de búsqueda
        return []

    def answer(self, query):
        """
        Fase 3: Generación
        Debe usar un LLM (OpenAI recomendado) para responder la pregunta usando el contexto recuperado.
        :return: String con la respuesta final.
        """
        # TODO: Implementar lógica de RAG (Contexto + LLM)
        return "Respuesta pendiente de implementación."

# Bloque para pruebas manuales del candidato
if __name__ == "__main__":
    pass
