import litellm
from gloabl import *

class OllamaEmbedding:
    def __init__(self, model=ollama_embedding_model):
        self.model = model

    def embed(self, text):
        response = litellm.embedding(
            model=self.model,
            input=text,
            api_base=f"{ollama_api_base}",
        )
        return response