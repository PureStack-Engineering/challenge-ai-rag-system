# 🧠 PureStack AI Engineering Challenge: The RAG Protocol

**PureStack.es - Engineering Validation Protocol.**
> *"We don't look for Prompt Engineers. We audit AI Engineers."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol.
This assessment is designed to audit your ability to build **Retrieval-Augmented Generation (RAG)** systems.

We are not looking for a 10-line script calling OpenAI. We are auditing your **architectural choices**, your understanding of **embeddings**, and your ability to apply **Software Engineering** principles to AI.

### 🚦 Certification Levels (Choose your Difficulty)
State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Core Functionality.
* **Requirement:** Implement the `RAGSystem` class to pass the automated tests.
* **Tasks:**
    1.  **Ingestion:** Read `data/test_knowledge.txt` and split it into chunks.
    2.  **Vector Store:** Store embeddings (using ChromaDB, FAISS, or simple in-memory vectors).
    3.  **Retrieval:** Implement the `query(question)` method to retrieve context and generate an answer.
* **Deliverable:** A script that passes the **Mocked Tests** (Green light on GitHub Actions).

#### 🥈 Level 2: Pro / Senior
* **Focus:** Robustness & Hallucination Management.
* **Requirement:** Everything in Level 3 + **Defensive AI**.
* **Extra Tasks:**
    1.  **Source Tracking:** The system must indicate *which* chunk provided the answer.
    2.  **Hallucination Control:** If the answer is NOT in the text, the system must return a specific fallback message (e.g., "Information not found in context") instead of inventing facts.
* **Deliverable:** Defensive logic handled within the `RAGSystem` class.

#### 🥇 Level 1: Elite / Architect
* **Focus:** API & Systems Engineering.
* **Requirement:** Everything above + **REST API**.
* **Extra Tasks:**
    1.  **FastAPI Wrapper:** Implement `main_api.py` to expose endpoints:
        * `POST /ingest`: Triggers document processing.
        * `POST /ask`: Accepts `{"question": "..."}` and returns the answer.
    2.  **Optimization:** Implement a generic Interface for the LLM to allow swapping models easily (e.g., swapping OpenAI for a local Llama model).
* **Deliverable:** A production-ready API structure.

---

### 🛠️ Tech Stack & Constraints
* **Language:** Python 3.10+
* **Allowed Frameworks:** LangChain, LlamaIndex, or raw Python (Your choice).
* **Vector Database:** ChromaDB (Preferred), FAISS, or In-Memory.
* **LLM:** OpenAI (`gpt-3.5` / `gpt-4`).

> **⚠️ IMPORTANT: The Automated Auditor (Tests)**
> The tests in this repository use **MOCKING**. They do *not* make real calls to OpenAI to avoid costs during evaluation.
> * **Locally:** You will need your own `OPENAI_API_KEY` to verify it works.
> * **On GitHub:** The tests check if your *logic* calls the LLM correctly, not the actual LLM output.

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  **Implement your solution** inside `rag_system.py`.
    * *Constraint:* You MUST keep the class name `RAGSystem` and the method `answer(query)` for tests to work.
4.  Run local tests: `pytest`.
5.  Submit your **Pull Request**.

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Architecture** | 35% | Separation of Ingestion vs Querying. |
| **Code Quality** | 25% | Type hinting, error handling, clean imports. |
| **RAG Logic** | 25% | Chunking strategy and retrieval efficiency. |
| **Testing** | 15% | Does it pass the CI/CD pipeline? |

---

### 🚨 Project Structure (Strict)
To ensure our **Automated Auditor** works, keep this structure:

```text
/
├── .github/workflows/   # PureStack Audit System (CI Pipeline)
├── data/
│   └── test_knowledge.txt # Source of Truth (The document to "learn")
├── tests/
│   └── test_rag.py      # Validation Tests (Mocked)
├── rag_system.py        # <--- YOUR CODE HERE (Class RAGSystem)
├── main_api.py          # <--- Skeleton for Level 1 (FastAPI)
├── requirements.txt     # <--- Dependencies
└── README.md
