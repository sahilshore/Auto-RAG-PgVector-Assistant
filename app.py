from typing import List
import nest_asyncio
import logging
import os
from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.document import Document
from phi.document.reader.pdf import PDFReader
from phi.knowledge import AssistantKnowledge
from phi.tools.duckduckgo import DuckDuckGo

from phi.llm.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder

from phi.vectordb.pgvector import PgVector2
from phi.storage.assistant.postgres import PgAssistantStorage

# -------------------------------------------------
# Load environment variables
# -------------------------------------------------
load_dotenv()

logger = logging.getLogger(__name__)

# Docker PostgreSQL (pgvector)
DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# -------------------------------------------------
# Setup Assistant
# -------------------------------------------------
def setup_assistant() -> Assistant:
    llm = OpenAIChat(
        model=os.getenv("OPENAI_MODEL_NAME", "gpt-4o"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    return Assistant(
        name="auto_rag_openai",
        llm=llm,
        storage=PgAssistantStorage(
            table_name="auto_rag_assistant_openai_final",
            db_url=DB_URL,
        ),
        knowledge_base=AssistantKnowledge(
            vector_db=PgVector2(
                db_url=DB_URL,
                # ⚠ NEW collection name (important)
                collection="auto_rag_documents_openai_final",
                embedder=OpenAIEmbedder(
                    model="text-embedding-3-small",
                    api_key=os.getenv("OPENAI_API_KEY"),
                ),
            ),
            num_documents=3,
        ),
        description="AutoRAG assistant using OpenAI embeddings + OpenAI LLM.",
        instructions=[
            "Always search the knowledge base first.",
            "If no relevant information is found, search the web.",
            "Ask clarifying questions if needed.",
            "Give clear and concise answers.",
        ],
        tools=[DuckDuckGo()],
        search_knowledge=True,
        read_chat_history=True,
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
    )

# -------------------------------------------------
# Add PDF to Knowledge Base
# -------------------------------------------------
def add_document_to_kb(assistant: Assistant, file_path: str):
    reader = PDFReader()
    documents: List[Document] = reader.read(file_path)

    if documents:
        assistant.knowledge_base.load_documents(documents, upsert=True)
        logger.info(f"Added document: {file_path}")
    else:
        logger.error("Failed to read PDF")

# -------------------------------------------------
# Query Assistant
# -------------------------------------------------
def query_assistant(assistant: Assistant, question: str) -> str:
    response = ""
    for delta in assistant.run(question):
        response += delta
    return response

# -------------------------------------------------
# Main
# -------------------------------------------------
if __name__ == "__main__":
    nest_asyncio.apply()

    assistant = setup_assistant()

    # Make sure sample.pdf exists in same folder
    add_document_to_kb(assistant, "sample.pdf")

    query = "What is the main topic of the document?"
    answer = query_assistant(assistant, query)

    print("\nQuestion:", query)
    print("Answer:", answer)
