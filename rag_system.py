import os
import openai

# --- IMPORTS ACTUALIZADOS (VERSIÓN 2024/2025) ---
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
# Aquí estaba el fallo: ahora se importa desde langchain_text_splitters
from langchain_text_splitters import CharacterTextSplitter
# ------------------------------------------------

class RAGSystem:
    def __init__(self, knowledge_path):
        self.knowledge_path = knowledge_path
        self.vector_db = None
        # Modelo local para evitar errores de API Key en los tests
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
        # Nota: Usamos la configuración por defecto de Chroma
        self.vector_db = Chroma.from_documents(
            documents=docs, 
            embedding=self.embedding_function,
            collection_name="purestack_audit"
        )
        print("✅ Ingesta completada.")

    def retrieve(self, query, top_k=1):
        """Busca en la base vectorial."""
        if not self.vector_db:
            # Intento de auto-recuperación si olvidaron llamar a ingest
            try:
                self.ingest()
            except:
                raise Exception("La base de datos no está inicializada. Ejecuta ingest() primero.")
        
        results = self.vector_db.similarity_search(query, k=top_k)
        return [doc.page_content for doc in results]

    def answer(self, query):
        """Genera respuesta (Mockeada en el test)."""
        context_docs = self.retrieve(query)
        context_text = "\n".join(context_docs)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Contexto: {context_text}"},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    pass
