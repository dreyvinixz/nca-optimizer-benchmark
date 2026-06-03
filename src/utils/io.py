"""I/O helpers for configuration and machine-readable experiment outputs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def project_path(path: str | Path) -> Path:
    """Resolve a repository-relative path."""
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return PROJECT_ROOT / candidate


def load_yaml(path: str | Path) -> dict[str, Any]:
    with project_path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data


def load_project_configs() -> dict[str, Any]:
    return {
        "paths": load_yaml("config/paths.yaml"),
        "experiment": load_yaml("config/experiment_config.yaml"),
        "search_spaces": load_yaml("config/search_spaces.yaml"),
    }


def ensure_directory(path: str | Path) -> Path:
    resolved = project_path(path)
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def ensure_output_directories(paths_config: dict[str, Any]) -> None:
    for group in ("outputs", "checkpoints", "logs"):
        for value in paths_config.get(group, {}).values():
            ensure_directory(value)


def save_csv(rows: list[dict[str, Any]], path: str | Path) -> None:
    resolved = project_path(path)
    resolved.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(resolved, index=False)


def write_text(path: str | Path, content: str) -> None:
    resolved = project_path(path)
    resolved.parent.mkdir(parents=True, exist_ok=True)
    resolved.write_text(content, encoding="utf-8")
