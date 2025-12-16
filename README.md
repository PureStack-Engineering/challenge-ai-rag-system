# 🧠 PureStack AI Engineering Challenge: The RAG Protocol

**PureStack.es - Engineering Validation Protocol.**
> *"We don't look for Prompt Engineers. We audit AI Engineers."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol.
This assessment is designed to audit your ability to build **Retrieval-Augmented Generation (RAG)** systems.

We are not looking for a 10-line script calling OpenAI. We are auditing your **architectural choices**, your understanding of **embeddings**, and your ability to apply **Software Engineering** principles to AI.

### 🚦 Certification Levels (Choose your Difficulty)
This challenge is scalable. Your seniority level will be determined by how far you take your solution. Please state in your Pull Request which level you are aiming for.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Core Functionality.
* **Requirement:** Implement the `RAGSystem` class to pass the automated tests (`pytest`).
* **Tasks:**
    1.  **Ingestion:** Read a text file and split it into chunks.
    2.  **Vector Store:** Store embeddings (using ChromaDB, FAISS, or in-memory).
    3.  **Simple RAG:** Retrieve relevant context and generate an answer using an LLM.
* **Deliverable:** Clean code that works and gets the **GREEN** light on GitHub Actions.

#### 🥈 Level 2: Pro / Senior
* **Focus:** Robustness, Traceability, and "Clean Code".
* **Requirement:** Everything in Level 3 + **Citations & Hallucination Management**.
* **Extra Tasks:**
    1.  **Source Citations:** The system must not only answer but indicate *where* in the text the info came from (e.g., `[Source: Chunk 2]`).
    2.  **Graceful Fallback:** If the answer is NOT in the provided text, the system must explicitly state "I don't have enough information", preventing hallucinations.
* **Deliverable:** Defensive coding logic and proper exception handling.

#### 🥇 Level 1: Elite / Architect
* **Focus:** System Engineering, API Exposure & Optimization.
* **Requirement:** Everything above + **API Wrapper & Search Strategy**.
* **Extra Tasks:**
    1.  **FastAPI Wrapper:** Expose your `RAGSystem` class as a functional REST API (`/ask`, `/ingest`).
    2.  **Retrieval Optimization:** Implement a **Hybrid Search** strategy (Keyword + Semantic) or document a significant improvement in retrieval (e.g., Re-ranking, Dynamic Chunking).
* **Deliverable:** A production-ready system, scalable and well-documented.

---

### 🛠️ Tech Stack & Constraints
* **Language:** Python 3.10+
* **Allowed Frameworks:** LangChain, LlamaIndex, or raw Python (Your choice demonstrates your criteria).
* **Vector Database:** ChromaDB (Preferred for simplicity), FAISS, or in-memory implementation.
* **LLM:** OpenAI (`gpt-3.5` / `gpt-4`).
    * *Note:* The automated tests in this repo use **Mocking**. They validate your logic without consuming real API credits. However, for local development, you will need your own API Key.

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  **Implement your solution** inside `rag_system.py`. The `RAGSystem` class structure is mandatory for the automated auditor.
4.  Run local tests: `pytest`.
5.  Submit your **Pull Request** stating the level achieved (1, 2, or 3).

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Functionality** | 30% | Do tests pass? Does it answer correctly? |
| **Code Quality** | 30% | Separation of concerns (Ingest vs. Query). Type Hinting. |
| **RAG Logic** | 25% | How do you handle Embeddings? Is retrieval efficient? |
| **Documentation** | 15% | Clarity in README and commits (Crucial for Level 1 & 2). |

---

### 🚨 Project Structure (DO NOT MODIFY)
To ensure our **Automated Auditor** works, keep this structure intact:

```text
/
├── .github/workflows/   # PureStack Audit System (DO NOT TOUCH)
├── tests/
│   ├── __init__.py
│   └── test_rag.py      # Validation Tests (Mocked LLM calls)
├── data/
│   └── test_knowledge.txt # Test Document (Source of Truth)
├── rag_system.py        # <--- YOUR CODE HERE (Class RAGSystem)
├── main_api.py          # <--- Skeleton for Level 1 (FastAPI)
├── requirements.txt     # <--- Add your libraries here
└── README.md
