"""Scene — a logical segment of the animation with its own prompt context."""
from __future__ import annotations
from dataclasses import dataclass, field
from src.core.frame import Frame

@dataclass
class Scene:
    """A contiguous group of frames sharing a visual/narrative context."""
    scene_id: str
    description: str
    base_prompt: str
    negative_prompt: str = ""
    duration_seconds: float = 2.0
    transition: str = "cut"
    frames: list[Frame] = field(default_factory=list)
    style_tags: list[str] = field(default_factory=list)
