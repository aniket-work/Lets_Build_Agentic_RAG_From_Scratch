import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        'hugging_face_token': os.getenv('HUGGING_FACE_TOKEN'),
        'knowledge_base_path': 'aniket_article_knowledge_base/dataset.json',
        'embedding_model_name': 'thenlper/gte-small',
        'vector_store_path': 'vector_store',
        'llm_model_name': 'llama3.1'
    }