from typing import List,Dict
import faiss
import numpy as np
from langchain_core.documents import Document

class FaissVectorStore:
    def __init__(self,embedding_dim:int):
        self.index=faiss.IndexFlatIP(embedding_dim)
        self.documents:List[Document]=[]

    def add(self,embeddings:np.ndarray,documents:List[Document]):
        if embeddings.shape[0]!=len(documents):
            raise ValueError("Embeddings and documents count mismatch")
        self.index.add(embeddings.astype("float32"))
        self.documents.extend(documents)
        print(f"[INFO] Added {len(documents)} vectors to Faiss index")

    def search(self,query_embedding:np.ndarray,top_k:int=5)->List[Dict]:
        """
        Search for similar documents using FAISS
        """
        scores,indices=self.index.search(
            query_embedding.astype("float32"),top_k
        )
        results=[]
        for idx,score in zip(indices[0],scores[0]):
            results.append({
                "score":float(score),
                "document":self.documents[idx]
            })
        return results
