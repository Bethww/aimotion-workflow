"""Frame Interpolator — fills gaps between keyframes for smooth animation."""
from __future__ import annotations
from src.core.timeline import Timeline

class FrameInterpolator:
    def __init__(self, method: str = "rife") -> None:
        self.method = method

    async def interpolate(self, timeline: Timeline) -> Timeline:
        # TODO: implement interpolation logic
        raise NotImplementedError
