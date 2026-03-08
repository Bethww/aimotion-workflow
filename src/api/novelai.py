"""NovelAI image-generation adapter (placeholder)."""
from __future__ import annotations
from src.api.base import BaseAPIAdapter
from src.models.schemas import GenerationRequest, GenerationResponse

class NovelAIAdapter(BaseAPIAdapter):
    def __init__(self, api_key: str, base_url: str = "https://api.novelai.net") -> None:
        self.api_key = api_key
        self.base_url = base_url

    async def generate(self, request: GenerationRequest) -> GenerationResponse:
        raise NotImplementedError

    async def health_check(self) -> bool:
        raise NotImplementedError

    def estimate_cost(self, request: GenerationRequest) -> float:
        return 0.0
