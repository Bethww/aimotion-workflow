# 🎬 AI Anime Workflow

An end-to-end pipeline for generating anime-style video and animation using API-based AI services. From text prompts to finished animated sequences — orchestrated, composable, and extensible.

---

## Overview

AI Anime Workflow provides a modular pipeline that connects to external AI generation APIs (NovelAI, niji·journey, Stability AI, etc.) to produce anime-style animations and video. It handles the full lifecycle: prompt engineering → frame generation → post-processing → video assembly.

```
[Prompt] → [Scene Planner] → [Frame Generator] → [Interpolator] → [Compositor] → [Video Encoder] → output.mp4
```

## Features

- **Multi-API support** — Pluggable adapters for NovelAI, niji·journey, Stability AI, and custom endpoints
- **Scene planning** — Break storyboards into keyframes with automatic prompt sequencing
- **Frame interpolation** — Smooth transitions between generated keyframes
- **Style consistency** — Maintain character/style coherence across frames via seed & prompt management
- **Batch processing** — Queue-based generation with retry logic and rate limiting
- **Video assembly** — FFmpeg-based compositing with configurable resolution, FPS, and codecs
- **Simple demo UI** — Browser-based interface for quick experimentation

## Quick Start

### Prerequisites

- Python 3.10+
- FFmpeg installed and on PATH
- API key(s) for your chosen generation service

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/ai-anime-workflow.git
cd ai-anime-workflow
pip install -e ".[dev]"
```

### Configuration

```bash
cp config/settings.example.yaml config/settings.yaml
# Edit config/settings.yaml with your API keys and preferences
```

### Basic Usage

```bash
# Generate a short animation from a prompt
python -m src.pipeline.run --prompt "a girl running through cherry blossoms, anime style" --frames 24 --output output.mp4

# Run from a storyboard file
python -m src.pipeline.run --storyboard examples/prompts/sample_storyboard.yaml

# Launch the demo UI
python -m demo.app
```

## Project Structure

```
ai-anime-workflow/
├── src/
│   ├── api/            # API client adapters (NovelAI, Stability, etc.)
│   ├── core/           # Core abstractions: Frame, Scene, Timeline
│   ├── models/         # Data models and schemas
│   ├── pipeline/       # Orchestration: planning → generation → assembly
│   └── utils/          # Helpers: rate limiting, image processing, logging
├── config/             # YAML configs and environment templates
├── demo/               # Lightweight browser-based demo UI
├── docs/               # Architecture docs and API reference
├── scripts/            # Dev/ops scripts (setup, benchmarks, etc.)
├── tests/              # Unit and integration tests
└── examples/           # Sample prompts, storyboards, and outputs
```

## Documentation

- [Architecture Overview](docs/architecture/README.md)
- [Pipeline Deep Dive](docs/architecture/pipeline.md)
- [API Adapter Guide](docs/api-reference/README.md)
- [Contributing](CONTRIBUTING.md)

## Roadmap

- [ ] Core pipeline MVP (prompt → keyframes → video)
- [ ] NovelAI adapter
- [ ] Stability AI adapter
- [ ] Frame interpolation (RIFE / FILM)
- [ ] Style-consistency module (character sheets, LoRA references)
- [ ] Audio sync support
- [ ] Demo UI with live preview
- [ ] CI/CD pipeline with automated tests
- [ ] Docker containerization

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
