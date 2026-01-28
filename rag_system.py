import os


class RAGSystem:
    """
    Main class for the PureStack RAG system.
    The candidate must complete the ingest, retrieve, and answer methods.
    """

    def __init__(self, knowledge_path):
        """
        Initializes the system.
        :param knowledge_path: Path to the text file containing the base knowledge.
        """
        self.knowledge_path = knowledge_path
      
        pass

    def ingest(self):
        """
        Phase 1: Ingestion
        Must load the text file, split it into chunks, and save it into the vector store.
        """
       
        raise NotImplementedError("You must implement the ingest() method.")

    def retrieve(self, query, top_k=1):
        """
        Phase 2: Retrieval
        Must search for the most relevant documents for the query.
        :return: List of strings with the content of the retrieved documents.
        """
    
        return []

    def answer(self, query):
        """
        Phase 3: Generation
        Must use an LLM (OpenAI recommended) to answer the question using the retrieved context.
        :return: String with the final answer.
        """
    
        return "Answer pending implementation."

# Block for candidate's manual testing
if __name__ == "__main__":
    pass
