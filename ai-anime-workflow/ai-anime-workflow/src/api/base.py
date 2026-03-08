"""Abstract base class for all API adapters."""
from __future__ import annotations
from abc import ABC, abstractmethod
from src.models.schemas import GenerationRequest, GenerationResponse

class BaseAPIAdapter(ABC):
    """Interface that every generation-API adapter must implement."""

    @abstractmethod
    async def generate(self, request: GenerationRequest) -> GenerationResponse: ...

    @abstractmethod
    async def health_check(self) -> bool: ...

    @abstractmethod
    def estimate_cost(self, request: GenerationRequest) -> float: ...
