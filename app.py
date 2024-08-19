import logging
from config import load_config
from logger import setup_logger
from data_loader import load_documents
from embedding import setup_embedding_model
from vector_store import setup_vector_store
from retriever import RetrieverTool
from agent import setup_agent, run_agentic_rag
from rag import run_standard_rag


def main():
    config = load_config()
    logger = setup_logger()

    logger.info("Loading documents...")
    documents = load_documents(config['knowledge_base_path'])

    logger.info("Setting up embedding model...")
    embedding_model = setup_embedding_model(config['embedding_model_name'])

    logger.info("Setting up vector store...")
    vector_store = setup_vector_store(documents, embedding_model, config['vector_store_path'])

    retriever_tool = RetrieverTool(vector_store)

    logger.info("Setting up agent...")
    agent_executor = setup_agent(retriever_tool, config['llm_model_name'])

    question = "Is there any framework automatically generate workflows for AI Agents?"

    logger.info("Running Agentic RAG...")
    agentic_answer = run_agentic_rag(agent_executor, question)

    logger.info("Running Standard RAG...")
    standard_answer = run_standard_rag(retriever_tool, question, config['llm_model_name'])

    print("Agentic RAG Answer:")
    print(agentic_answer)

    print("\nStandard RAG Answer:")
    print(standard_answer)


if __name__ == "__main__":
    main()