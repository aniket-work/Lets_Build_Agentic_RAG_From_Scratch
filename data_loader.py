import json
from langchain.schema import Document

def load_documents(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        knowledge_base = json.load(file)

    return [
        Document(page_content=doc["text"], metadata={"source": doc["source"].split("/")[-1]})
        for doc in knowledge_base
    ]