import json
from src.loader import load_resume, load_jobdescription
from src.chunker import chunk_document
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.matcher import ResumeJDMatcher
from src.llm_explainer import LLMExplainer
from langchain_core.documents import Document


def run_pipeline(resume_text: str, job_description_text: str):

    # Create proper Document objects
    resume_docs = [Document(page_content=resume_text)]
    jd_docs = [Document(page_content=job_description_text)]

    resume_chunks = chunk_document(resume_docs)
    jd_chunks = chunk_document(jd_docs)

    embedding_pipeline = EmbeddingPipeline()
    resume_embeddings = embedding_pipeline.embed_chunks(resume_chunks)
    jd_embeddings = embedding_pipeline.embed_chunks(jd_chunks)

    embedding_dim = resume_embeddings.shape[1]
    vector_store = FaissVectorStore(embedding_dim=embedding_dim)
    vector_store.add(resume_embeddings, resume_chunks)

    matcher = ResumeJDMatcher(vector_store=vector_store)
    match_results = matcher.match(
        jd_embeddings=jd_embeddings,
        jd_chunks=jd_chunks,
        top_k=3
    )

    explainer = LLMExplainer()
    final_report = explainer.explain(match_results)

    return final_report


def main():
    result = run_pipeline()
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()