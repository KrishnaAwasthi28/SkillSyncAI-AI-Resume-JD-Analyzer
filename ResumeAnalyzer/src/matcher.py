from typing import List,Dict
import numpy as np
from langchain_core.documents import Document
from src.vectorstore import FaissVectorStore

class ResumeJDMatcher:
    def __init__(self,vector_store:FaissVectorStore,strong_threshold:float=0.7,weak_threshold:float=0.4):
        self.vector_store=vector_store
        self.strong_threshold=strong_threshold
        self.weak_threshold=weak_threshold

    def match(self,jd_embeddings:np.ndarray,jd_chunks:List[Document],top_k:int=3)->List[Dict]:
        """
        Match JD chunks against resume vector store
        """
        results=[]
        for i,jd_embedding in enumerate(jd_embeddings):
            search_results=self.vector_store.search(jd_embedding.reshape(1,-1),top_k=top_k)
            best=search_results[0]
            score=best["score"]

            if score >= self.strong_threshold:
                match_type="MATCH"
            elif score >= self.weak_threshold:
                match_type="PARTIAL MATCH"
            else:
                match_type="MISSING"
            
            results.append({
                "jd_text":jd_chunks[i].page_content,
                "status":match_type,
                "score":score,
                "evidence":best["document"].page_content
            })
        return results


        