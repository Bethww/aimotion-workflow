"""Configuration loader — reads YAML settings and environment variables."""
from __future__ import annotations
from pathlib import Path
import yaml

def load_config(path: Path = Path("config/settings.yaml")) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Config not found at {path}. Copy config/settings.example.yaml.")
    with open(path) as f:
        return yaml.safe_load(f)
