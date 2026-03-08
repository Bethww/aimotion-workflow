"""Compositor — assembles frames into final video output via FFmpeg."""
from __future__ import annotations
from pathlib import Path
from src.core.timeline import Timeline

class Compositor:
    def __init__(self, fps: int = 12, codec: str = "libx264", output_format: str = "mp4") -> None:
        self.fps = fps
        self.codec = codec
        self.output_format = output_format

    async def compose(self, timeline: Timeline, output_path: Path) -> Path:
        # TODO: implement FFmpeg-based video encoding
        raise NotImplementedError
