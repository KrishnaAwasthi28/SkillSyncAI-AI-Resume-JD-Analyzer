from typing import Dict, Any,List
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
import json
from dotenv import load_dotenv
from src.schemas import AnalysisResponse

load_dotenv()


class LLMExplainer:
    def __init__(
        self,
        model_name: str = "openai/gpt-oss-120b",
        temperature: float = 0.2,
    ):
        self.llm = ChatGroq(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv("GROQ_API_KEY"),
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are an ATS resume evaluator.

            Analyze the resume and job description match information below.

            Return ONLY valid JSON.
            Do not return markdown.
            Do not add explanation outside JSON.

            The candidate name is typically at the top of the resume.
            Extract it explicitly.
            If not found, return empty string.

            Return output in this exact format:

            {{
            "status": "FULL_MATCH | PARTIAL_MATCH | LOW_MATCH",
            "score": integer between 0 and 100,
            "strengths": ["point1", "point2"],
            "gaps": ["point1", "point2"],
            "recommendations": ["point1", "point2"]
            }}

            Match Data (Multiple Requirements):
            {jd_text}
            """
)

    def explain(self, match_results: List[Dict[str, Any]]) -> Dict[str, Any]:

        combined_text = ""
        for idx, result in enumerate(match_results, start=1):
            combined_text += f"""
            Requirement {idx}:
            JD Requirement: {result['jd_text']}
            Match Status: {result['status']}
            Similarity Score (0-1): {round(result['score'], 2)}
            Evidence: {result['evidence']}
            -----------------------------------
            """

        chain = self.prompt | self.llm

        raw_response = chain.invoke({
            "jd_text": combined_text
        })

        content = raw_response.content.strip()

        if content.startswith("```"):
            content = content.replace("```json", "").replace("```", "").strip()

        try:
            parsed_json = json.loads(content)
        except json.JSONDecodeError:
            raise ValueError("LLM did not return valid JSON:\n" + content)

        # 🚀 Enterprise Validation
        validated_response = AnalysisResponse(**parsed_json)

        return validated_response.dict()