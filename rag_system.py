import os
import openai
# --- CORRECCIONES DE IMPORTACIÓN PARA LANGCHAIN NUEVO ---
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
# ---------------------------------------------------------

class RAGSystem:
    def __init__(self, knowledge_path):
        self.knowledge_path = knowledge_path
        self.vector_db = None
        # Usamos embeddings locales para evitar errores de API Key en el test
        self.embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    def ingest(self):
        """Carga el archivo, lo divide y crea la base de datos vectorial."""
        if not os.path.exists(self.knowledge_path):
            raise FileNotFoundError(f"No se encuentra el archivo: {self.knowledge_path}")

        # 1. Cargar Documento
        loader = TextLoader(self.knowledge_path, encoding="utf-8")
        documents = loader.load()

        # 2. Dividir en chunks
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        # 3. Crear Vector Store (en memoria)
        self.vector_db = Chroma.from_documents(
            documents=docs, 
            embedding=self.embedding_function,
            collection_name="purestack_audit"
        )
        print("✅ Ingesta completada.")

    def retrieve(self, query, top_k=1):
        """Busca en la base vectorial."""
        if not self.vector_db:
            raise Exception("La base de datos no está inicializada. Ejecuta ingest() primero.")
        
        results = self.vector_db.similarity_search(query, k=top_k)
        return [doc.page_content for doc in results]

    def answer(self, query):
        """Genera respuesta (Mockeada en el test)."""
        context_docs = self.retrieve(query)
        context_text = "\n".join(context_docs)

        # Esta llamada fallaría sin API Key real, pero el test la intercepta (mock)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Contexto: {context_text}"},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

# Bloque para ejecución manual
if __name__ == "__main__":
    # Asegúrate de que existe data/test_knowledge.txt si lo corres en local
    pass
