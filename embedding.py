from langchain_huggingface import HuggingFaceEmbeddings

def setup_embedding_model(model_name):
    return HuggingFaceEmbeddings(model_name=model_name)