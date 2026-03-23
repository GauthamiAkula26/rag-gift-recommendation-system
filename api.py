from __future__ import annotations

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.service import GiftRecommendationService

app = FastAPI(title="RAG Gift Recommendation API", version="1.0.0")
service = GiftRecommendationService()


class RecommendationRequest(BaseModel):
    gifter_id: str = Field(default="U100")
    recipient_id: str = Field(default="U101")
    occasion: Literal["birthday", "holiday", "anniversary", "selfcare", "casual"] = "birthday"
    min_budget: float = 20.0
    max_budget: float = 80.0
    top_k: int = 5


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/recommend")
def recommend(request: RecommendationRequest) -> dict:
    return service.recommend(
        gifter_id=request.gifter_id,
        recipient_id=request.recipient_id,
        occasion=request.occasion,
        budget=(request.min_budget, request.max_budget),
        top_k=request.top_k,
    )
