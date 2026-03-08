from src.pipeline.planner import ScenePlanner
from src.models.schemas import StoryboardEntry

def test_full_plan_smoke():
    planner = ScenePlanner()
    entries = [
        StoryboardEntry(scene_id="intro", description="Opening", prompt="sunset, anime", duration=1.5),
        StoryboardEntry(scene_id="action", description="Chase", prompt="running, anime", duration=3.0),
    ]
    timeline = planner.plan(entries)
    assert len(timeline.scenes) == 2
    assert timeline.total_frames > 0
