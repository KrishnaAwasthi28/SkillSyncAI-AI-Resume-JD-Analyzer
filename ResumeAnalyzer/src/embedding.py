from typing import List
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingPipeline:
    def __init__(self, model_name:str="all-MiniLM-L6-v2"):
        self.model=SentenceTransformer(model_name)
        print(f"[DEBUG] Loaded embedding model:{model_name}")

    def embed_chunks(self,chunks:List[Document])->np.ndarray:
        """
        Applying embeddings to created chunks 
        """
        texts=[chunk.page_content for chunk in chunks]
        print(f"[INFO] Generating embeddings for {len(texts)} chunks ...")
        embeddings=self.model.encode(texts,show_progress_bar=True,normalize_embeddings=True)
        print(f"[INFO] Embeddings shape: {embeddings.shape}")
        return embeddings