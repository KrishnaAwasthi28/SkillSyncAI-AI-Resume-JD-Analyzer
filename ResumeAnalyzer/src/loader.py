from pathlib import Path
from typing import List,Any
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain_core.documents import Document

def load_resume(data_dir:str)->List[Document]:
    """
    Load all the text from the resume pdf and convert to langchain document structure
    """
    resume_dir=Path(data_dir).resolve()
    print(f"[DEBUG] Data path:{resume_dir}")
    document=[]
    pdf_files=list(resume_dir.glob("*.pdf"))
    if not pdf_files:
        raise FileNotFoundError("No PDF files found in the directory")
    try:
        loader=PyPDFLoader(str(pdf_files[0]))
        loaded=loader.load()
        print("[DEBUG] loaded text from resume")
        document.extend(loaded)
    except Exception as e:
        raise RuntimeError(f"Failed to load resume PDF: {e}")
    return document

def load_jobdescription(data_dir:str)->List[Document]:
    """
    Load all the text from the job description text and convert into langchain document structure"""
    jobdesc_path=Path(data_dir).resolve()
    print(f"[DEBUG] data path : {jobdesc_path}")
    document=[]
    txt_files=list(jobdesc_path.glob("*.txt"))
    if not txt_files:
        raise FileNotFoundError("No text files found in the directory")
    try:
        loader=TextLoader(str(txt_files[0]),encoding="utf-8")
        loaded=loader.load()
        print("[DEBUG] loaded text from job description")
        document.extend(loaded)
    except Exception as e:
        raise RuntimeError(f"Failed to load job description: {e}")    
    return document