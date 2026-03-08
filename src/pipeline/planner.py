"""Scene Planner — converts a storyboard into a concrete frame-by-frame timeline."""
from __future__ import annotations
from src.core.frame import Frame
from src.core.scene import Scene
from src.core.timeline import Timeline
from src.models.schemas import StoryboardEntry

class ScenePlanner:
    """Expands storyboard entries into a fully-specified Timeline with keyframes."""

    def __init__(self, fps: int = 12, keyframe_interval: int = 4) -> None:
        self.fps = fps
        self.keyframe_interval = keyframe_interval

    def plan(self, entries: list[StoryboardEntry]) -> Timeline:
        timeline = Timeline(title="Untitled", fps=self.fps)
        for entry in entries:
            total_frames = int(entry.duration * self.fps)
            frames = [
                Frame(index=i, prompt=entry.prompt, is_keyframe=(i % self.keyframe_interval == 0))
                for i in range(total_frames)
            ]
            scene = Scene(
                scene_id=entry.scene_id,
                description=entry.description,
                base_prompt=entry.prompt,
                negative_prompt=entry.negative_prompt,
                duration_seconds=entry.duration,
                transition=entry.transition,
                frames=frames,
                style_tags=entry.style_tags,
            )
            timeline.scenes.append(scene)
        return timeline
