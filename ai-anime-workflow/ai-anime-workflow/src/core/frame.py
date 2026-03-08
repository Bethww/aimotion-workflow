"""Frame representation — a single generated image in the timeline."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class Frame:
    """Represents one frame in an animation sequence."""
    index: int
    prompt: str
    image_path: Path | None = None
    seed: int | None = None
    is_keyframe: bool = False
    metadata: dict = field(default_factory=dict)

    @property
    def is_generated(self) -> bool:
        return self.image_path is not None and self.image_path.exists()
