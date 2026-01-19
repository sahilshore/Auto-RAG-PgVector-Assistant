# Auto RAG PgVector Assistant

A Retrieval-Augmented Generation (RAG) assistant that ingests PDF documents, stores embeddings in a vector database, and generates accurate, context-aware answers using Large Language Models.

---

## 📦 Components Included

### 1️ PDF Ingestion Module
- Reads and parses PDF documents  
- Splits documents into manageable text chunks  
- Prepares content for embedding  

**Tool Used:** PhiData PDFReader  

---

### 2️ Embedding Generator
- Converts text chunks into dense vector embeddings  
- Enables semantic understanding of documents  
- Uses OpenAI embedding model for high accuracy  

**Model Used:** text-embedding-3-small  
**Provider:** OpenAI  

---

### 3️ Vector Database (Knowledge Store)
- Stores document embeddings efficiently  
- Supports fast similarity search  
- Persists data across sessions  

**Database:** PostgreSQL  
**Extension:** pgvector  
**Deployment:** Docker  

---

### 4️ Retrieval-Augmented Generation (RAG) Engine
- Searches the vector database for relevant chunks  
- Retrieves top-K semantically similar results  
- Injects retrieved context into the LLM prompt  

**Retrieval Method:** Semantic Search  
**Vector DB:** PostgreSQL + pgvector  

---

### 5️ LLM Answer Generator
- Generates final answers using retrieved context  
- Produces concise, context-aware responses  
- Reduces hallucinations by grounding answers in documents  

**LLM Used:** gpt-4o  
**Provider:** OpenAI  

---

### 6️ Web Search Fallback Tool
- Performs internet search when knowledge base lacks information  
- Enhances answer completeness  
- Prevents incomplete responses  

**Tool Used:** DuckDuckGo Search  

---

## 🔌 LLM & Embedding Providers

This project uses cloud-based AI services:

- **OpenAI Embeddings** – High-quality semantic representations  
- **OpenAI LLM (gpt-4o)** – Accurate and reliable text generation  

> Switching models requires only configuration changes.

---

## 🛠️ Technology Stack

- **Python**
- **PhiData**
- **OpenAI API**
- **PostgreSQL**
- **pgvector**
- **Docker**
- **DuckDuckGo Search**
- **RAG (PDF-based Retrieval)**

---

## ⚙️ How To Use

1. Clone the repository  
2. Create and activate a Python virtual environment  
3. Install dependencies from `requirements.txt`  
4. Add OpenAI API credentials in a `.env` file  
5. Start PostgreSQL using Docker  
6. Add a PDF document  
7. Run `app.py`  

The assistant will ingest the PDF, store embeddings, and answer queries using the RAG pipeline.

---

##  Who This Is For

This project is suitable for:
- Students learning **Retrieval-Augmented Generation (RAG)**  
- Developers exploring **Vector Databases**  
- Engineers building **LLM-powered document assistants**  
- Anyone creating a **Generative AI portfolio project**  

---

## ⭐ Final Note

This repository goes beyond simple prompt engineering.  
It demonstrates a **real-world RAG architecture** where AI systems **retrieve relevant knowledge, reason over it, and generate reliable answers** using a vector database-backed knowledge base.
