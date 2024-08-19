from transformers import AutoTokenizer
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_text_splitter(tokenizer_name, hugging_face_token):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, token=hugging_face_token)
    return RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        tokenizer,
        chunk_size=200,
        chunk_overlap=20,
        add_start_index=True,
        strip_whitespace=True,
        separators=["\n\n", "\n", ".", " ", ""],
    )