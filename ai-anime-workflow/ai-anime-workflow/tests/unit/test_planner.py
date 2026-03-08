from src.models.schemas import StoryboardEntry
from src.pipeline.planner import ScenePlanner

def test_plan_creates_correct_frame_count():
    planner = ScenePlanner(fps=12, keyframe_interval=4)
    entries = [StoryboardEntry(scene_id="s1", description="Test", prompt="cherry blossoms", duration=2.0)]
    timeline = planner.plan(entries)
    assert len(timeline.scenes) == 1
    assert len(timeline.scenes[0].frames) == 24

def test_keyframes_are_marked_correctly():
    planner = ScenePlanner(fps=12, keyframe_interval=4)
    entries = [StoryboardEntry(scene_id="s1", description="Test", prompt="test", duration=1.0)]
    timeline = planner.plan(entries)
    keyframes = [f for f in timeline.scenes[0].frames if f.is_keyframe]
    assert len(keyframes) == 3
