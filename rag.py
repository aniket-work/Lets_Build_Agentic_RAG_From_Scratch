from langchain_community.llms import Ollama

def run_standard_rag(retriever_tool, question, llm_model_name):
    context = retriever_tool(question)

    prompt = f"""Given the question and the supporting documents provided below, deliver a comprehensive and concise answer. Ensure that your response is directly relevant to the question, and reference the source document number when applicable.

**Question:**  
{question}

**Supporting Documents:**  
{context}

"""

    llm_engine = Ollama(model=llm_model_name)
    return llm_engine(prompt)