from pathlib import Path


def should_exclude(path: Path, exclude_dirs: list[str]) -> bool:
    return any(excluded in path.parts for excluded in exclude_dirs)
