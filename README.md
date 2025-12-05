Policy Compliance Checker – Medical RAG (Task 2)

This project implements an automated Policy Compliance Checker using Google Gemini, FAISS vector search, and custom rule-based evaluation. The system checks medical text against a set of predefined policy rules and highlights compliant and non-compliant sections.

Project Features

1.Rule File (15+ Rules)
A structured JSON rule-set containing all policy rules such as:

Accuracy requirements

Forbidden content

Safety violations

Medical claims restrictions

Data privacy rules

2. PDF Ingestion + Vector Store Pipeline
The system:

Loads PDF files

Splits them using RecursiveCharacterTextSplitter

Generates embeddings using Google Generative AI Embeddings

Builds and saves a FAISS vector store for fast retrieval

Generated folder:

vectorstore/ index.faiss index.pkl

3. Custom Compliance Checker Tool
A multi-step rule evaluation pipeline:

Retrieves relevant chunks using FAISS

Uses Gemini to evaluate if content violates rules

Returns structured compliance results

Example output:

{ "rule_id": "R1", "is_compliant": true, "explanation": "No harmful medical advice found." }

4. Multi-Rule Agent Workflow
Your system:

Iterates through each rule

Applies Gemini-based reasoning

Produces a final compliance report

Evidence chunks

Model explanations

Example:

Rule ID Compliance Evidence Explanation R1 Not Compliant Chunk 12 Incorrect medical advice R2 Compliant Chunk 5 No privacy issues

Project Structure task2/ │ ├── rules.json # Contains 15+ policy rules ├── ingest.ipynb # PDF → Chunks → Embeddings → FAISS ├── compliance_checker.ipynb # Full compliance workflow ├── vectorstore/ # Saved FAISS index │ ├── index.faiss │ ├── index.pkl │ ├── app.py # Streamlit UI (optional) └── README.md # This file

Installation

1.Create virtual environment python -m venv venv
2.Activate Windows: venv\Scripts\activate
3.Install dependencies pip install -r requirements.txt Running the Project Run Ingestion python ingest.py
Run Compliance Checker python compliance_checker.py
Run Streamlit App python -m streamlit run app.py
