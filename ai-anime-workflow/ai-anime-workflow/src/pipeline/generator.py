"""Frame Generator — sends keyframe prompts to the API and saves results."""
from __future__ import annotations
from src.api.base import BaseAPIAdapter
from src.core.timeline import Timeline

class FrameGenerator:
    def __init__(self, adapter: BaseAPIAdapter) -> None:
        self.adapter = adapter

    async def generate_keyframes(self, timeline: Timeline) -> Timeline:
        # TODO: implement batch generation with rate limiting
        raise NotImplementedError
