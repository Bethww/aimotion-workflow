"""Request/response schemas for API interactions and storyboard files."""
from __future__ import annotations
from pydantic import BaseModel, Field

class GenerationRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""
    width: int = 1024
    height: int = 576
    steps: int = 28
    seed: int | None = None
    sampler: str = "k_euler_ancestral"
    model: str | None = None

class GenerationResponse(BaseModel):
    image_b64: str
    seed: int
    generation_time_ms: float = 0.0
    metadata: dict = Field(default_factory=dict)

class StoryboardEntry(BaseModel):
    scene_id: str
    description: str
    prompt: str
    negative_prompt: str = ""
    duration: float = 2.0
    transition: str = "cut"
    style_tags: list[str] = Field(default_factory=list)
