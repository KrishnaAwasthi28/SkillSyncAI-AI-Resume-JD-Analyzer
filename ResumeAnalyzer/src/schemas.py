from pydantic import BaseModel, Field
from typing import List, Literal


class AnalysisResponse(BaseModel):
    status: Literal["FULL_MATCH", "PARTIAL_MATCH", "LOW_MATCH"]
    score: int = Field(..., ge=0, le=100)
    strengths: List[str]
    gaps: List[str]
    recommendations: List[str]