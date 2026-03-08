# Contributing to AI Anime Workflow

Thanks for your interest in contributing! Here's how to get started.

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/ai-anime-workflow.git
cd ai-anime-workflow
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Branch Strategy

- `main` — stable releases
- `develop` — integration branch
- `feature/*` — new features
- `fix/*` — bug fixes

## Pull Request Process

1. Fork the repo and create your branch from `develop`
2. Write tests for any new functionality
3. Ensure all tests pass: `pytest`
4. Update documentation if needed
5. Submit a PR with a clear description

## Code Style

- Follow PEP 8
- Use type hints throughout
- Docstrings in Google style
- Run `ruff check .` before committing

## Reporting Issues

Open an issue with:
- A clear title and description
- Steps to reproduce (if a bug)
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
