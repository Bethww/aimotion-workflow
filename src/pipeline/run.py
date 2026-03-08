"""CLI entry point — ties the full pipeline together."""
from __future__ import annotations
import click

@click.command()
@click.option("--prompt", type=str, help="Single prompt for quick generation.")
@click.option("--storyboard", type=click.Path(exists=True), help="Path to storyboard YAML.")
@click.option("--frames", type=int, default=24, help="Number of frames to generate.")
@click.option("--output", type=click.Path(), default="output.mp4", help="Output video path.")
def main(prompt: str | None, storyboard: str | None, frames: int, output: str) -> None:
    """Run the AI Anime Workflow pipeline."""
    click.echo("🎬 AI Anime Workflow")
    click.echo(f"   Prompt:     {prompt or '(from storyboard)'}")
    click.echo(f"   Frames:     {frames}")
    click.echo(f"   Output:     {output}")
    click.echo("\n⚠️  Pipeline execution not yet implemented. See README for roadmap.")

if __name__ == "__main__":
    main()
