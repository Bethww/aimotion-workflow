#!/usr/bin/env bash
set -euo pipefail
echo "🎬 Setting up AI Anime Workflow..."
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
if [ ! -f config/settings.yaml ]; then
  cp config/settings.example.yaml config/settings.yaml
  echo "📝 Created config/settings.yaml — edit it with your API keys."
fi
echo "✅ Setup complete. Activate with: source .venv/bin/activate"
