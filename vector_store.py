import os
from langchain.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

def setup_vector_store(documents, embedding_model, store_path):
    if os.path.exists(store_path):
        return FAISS.load_local(store_path, embedding_model, allow_dangerous_deserialization=True)
    else:
        vectordb = FAISS.from_documents(
            documents=documents,
            embedding=embedding_model,
            distance_strategy=DistanceStrategy.COSINE,
        )
        vectordb.save_local(store_path)
        return vectordb