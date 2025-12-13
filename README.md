# 🤖 PureStack AI Engineering Challenge: The RAG Protocol

### Context
Welcome to the PureStack Technical Validation Protocol.
This assessment simulates a real-world scenario: building a **Retrieval-Augmented Generation (RAG)** system capable of ingesting corporate documents and answering questions with high accuracy.

**⚠️ Warning:** We do not look for "it works on my machine". We look for production-ready code, clean architecture, and handling of edge cases.

---

### 🎯 The Objective
Build a lightweight API (FastAPI/Flask) that exposes an endpoint to query a knowledge base.

1.  **Ingest:** Create a script to process a text file (simulated knowledge base), chunk it, and store embeddings in a Vector Database (ChromaDB, FAISS, or simple in-memory equivalent).
2.  **Retrieve:** When a user asks a question, find the most relevant context chunks.
3.  **Generate:** Synthesize an answer using an LLM (You can use OpenAI API, Ollama, or a Mock function if you don't have API keys).

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+
* **Framework:** FastAPI (Preferred) or Flask.
* **AI/Orchestration:** LangChain, LlamaIndex, or raw Python (your choice).
* **Vector Store:** Any local vector store (Chroma, FAISS, LanceDB).

### 🧪 Evaluation Criteria (How we audit you)
We run an automated suite of tests against your submission. We look for:

1.  **Code Quality:** PEP8 standards, type hinting (`typing`), and modularity.
2.  **RAG Logic:** Did you handle text splitting correctly? Is the retrieval logic sound?
3.  **Error Handling:** What happens if the LLM hallucinates or times out?
4.  **Documentation:** A clear `instructions.md` on how to run your API.

### 🚀 Getting Started

1.  **Fork** this repository.
2.  Create a virtual environment (`python -m venv venv`).
3.  Install your dependencies and freeze them in `requirements.txt`.
4.  Complete the challenge in the `src/` folder.
5.  Submit your solution via Pull Request or by sending the repo link.

---

### 📂 Bonus Points (Elite Level)
* Implement a **caching mechanism** to avoid re-generating answers for the same query.


* Add a **source citation** feature (return *which* chunk of text generated the answer).

> **PureStack Engineering.** Validated by Code.
