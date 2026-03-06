from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import io
import pdfplumber

from main import run_pipeline
from src.schemas import AnalysisResponse


app = FastAPI(title="Resume-JD Analyzer AI Microservice")


# 🔥 Enable CORS (Spring Boot will call this)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Utility: Extract text from PDF
def extract_text_from_pdf(file_bytes: bytes) -> str:
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(
    resume: UploadFile = File(...),
    jobDescription: str = Form(...)
):
    try:
        if not resume.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Resume must be a PDF file.")

        file_bytes = await resume.read()
        resume_text = extract_text_from_pdf(file_bytes)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Empty resume content.")

        result = run_pipeline(resume_text, jobDescription)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)