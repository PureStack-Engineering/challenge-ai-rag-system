import os
import openai

# --- IMPORTS CORREGIDOS PARA LANGCHAIN MODERNO ---
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
# ESTA ES LA LÍNEA QUE TE DABA ERROR, AHORA ESTÁ CORREGIDA:
from langchain_text_splitters import CharacterTextSplitter
# ------------------------------------------------

class RAGSystem:
    def __init__(self, knowledge_path):
        self.knowledge_path = knowledge_path
        self.vector_db = None
        # Modelo local
        self.embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    def ingest(self):
        if not os.path.exists(self.knowledge_path):
            raise FileNotFoundError(f"No se encuentra el archivo: {self.knowledge_path}")

        # 1. Cargar
        loader = TextLoader(self.knowledge_path, encoding="utf-8")
        documents = loader.load()

        # 2. Split (Ahora usa la librería correcta)
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        # 3. Vector Store
        self.vector_db = Chroma.from_documents(
            documents=docs, 
            embedding=self.embedding_function,
            collection_name="purestack_audit"
        )
        print("✅ Ingesta completada.")

    def retrieve(self, query, top_k=1):
        if not self.vector_db:
            try:
                self.ingest()
            except:
                raise Exception("DB no inicializada.")
        
        results = self.vector_db.similarity_search(query, k=top_k)
        return [doc.page_content for doc in results]

    def answer(self, query):
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
