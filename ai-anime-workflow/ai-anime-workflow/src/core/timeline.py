"""Timeline — the full ordered sequence of scenes that compose the animation."""
from __future__ import annotations
from dataclasses import dataclass, field
from src.core.scene import Scene

@dataclass
class Timeline:
    """Top-level container: an ordered list of scenes forming the complete video."""
    title: str
    scenes: list[Scene] = field(default_factory=list)
    fps: int = 12
    resolution: tuple[int, int] = (1024, 576)

    @property
    def total_frames(self) -> int:
        return sum(len(s.frames) for s in self.scenes)

    @property
    def duration_seconds(self) -> float:
        return sum(s.duration_seconds for s in self.scenes)
