# 🧠 PureStack AI Engineering Challenge: The RAG Protocol

### Context
Welcome to the **PureStack Technical Validation Protocol**.
This assessment is designed to audit your ability to build **AI-driven systems**, specifically Retrieval-Augmented Generation (RAG). We are not looking for "Prompt Engineers"; we are looking for **AI Engineers** who understand vector stores, embeddings, and retrieval logic.

**⚠️ The Standard:** We expect clean, modular code that handles the full RAG pipeline: Ingestion → Embedding → Retrieval → Generation.

---

### 🎯 The Objective
Build a Python class that ingests a textual knowledge base and answers questions about it using an LLM (OpenAI recommended) grounded in that data.

**The Mission:**
1.  **Ingest:** Read a text file, split it into chunks, and store embeddings in a Vector Database (ChromaDB recommended).
2.  **Retrieve:** Given a user query, find the most relevant chunks.
3.  **Generate:** Construct a prompt with the retrieved context and get an answer from the LLM.

---

**Requirement:** Your solution must be inside the file `rag_system.py` and the class must be named `RAGSystem`.

### 🛠️ Tech Stack Requirements
* **Language:** Python 3.10+
* **Frameworks:** You are free to use **LangChain**, **LlamaIndex**, or raw Python code.
* **Vector DB:** **ChromaDB** (preferred for simplicity), FAISS, or any in-memory store.
* **LLM:** OpenAI (`gpt-3.5` or `gpt-4`).
    * *Note:* The automated tests in this repo use **Mocking**. They verify your logic without needing a real API Key. However, for your local development, you will need your own key.

### 🧪 Evaluation Criteria (How we audit you)
We will clone your repo and run the automated audit (`pytest`). We look for:

* **Green Lights:** Your code must pass the provided GitHub Actions workflow.
* **Retrieval Accuracy:** Does your system find the correct text chunk for a specific query?
* **Code Quality:** Clean separation of concerns (Ingestion vs. Querying).
* **Dependency Management:** Your `requirements.txt` must work in a fresh environment.

### 🚀 Getting Started
1. **Fork** this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. **Implement your solution** inside `rag_system.py`. You need to complete:
    * `ingest()`
    * `retrieve(query)`
    * `answer(query)`
4. Run the tests locally: `pytest`.
5. Submit via Pull Request.

### 📂 Bonus Points (Elite Level)
* Implement **Hybrid Search** (Keyword + Semantic).
* Add **Source Citations** to the final answer (e.g., "Source: page 1").
* Wrap the system in a **FastAPI** endpoint.

---

### 🚨 CRITICAL: Project Structure
To ensure our **Automated Auditor** works correctly, you **MUST** follow this structure.
We have provided a skeleton in `rag_system.py`.

```text
/
├── .github/workflows/   # PureStack Audit System (DO NOT TOUCH)
├── tests/               # Validation Tests (Mocked LLM calls)
├── data/                # Place your test documents here
├── rag_system.py        # <--- YOUR CODE GOES HERE (Class RAGSystem)
├── requirements.txt     # <--- Add your dependencies here
└── README.md
