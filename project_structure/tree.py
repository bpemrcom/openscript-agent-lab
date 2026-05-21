"""Safe project tree builder for the Stage 2 viewer."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

DEFAULT_MAX_DEPTH = 6
DEFAULT_MAX_ENTRIES = 2000

_SENSITIVE_TOKENS = (
    "token",
    "tokens",
    "secret",
    "secrets",
    "key",
    "keys",
    "auth",
    "password",
    "credential",
    "credentials",
)

_SENSITIVE_TOKEN_RE = re.compile(
    r"(^|[^a-z0-9])(" + "|".join(map(re.escape, _SENSITIVE_TOKENS)) + r")([^a-z0-9]|$)"
)


def _is_hidden_name(name: str) -> bool:
    lowered = name.lower()
    if lowered == ".git":
        return True
    if lowered == ".env" or lowered.startswith(".env."):
        return True
    if lowered == "node_modules" or lowered == "__pycache__":
        return True
    if lowered.endswith(".pyc"):
        return True
    return bool(_SENSITIVE_TOKEN_RE.search(lowered))


def _is_within_root(path: Path, root: Path) -> bool:
    try:
        return path.resolve().is_relative_to(root)
    except AttributeError:
        resolved = path.resolve()
        return resolved == root or root in resolved.parents


def _build_dir(
    current: Path,
    root: Path,
    depth: int,
    state: dict[str, Any],
    max_depth: int,
    max_entries: int,
) -> dict[str, Any] | None:
    if state["count"] >= max_entries:
        return None

    node: dict[str, Any] = {"name": current.name or root.name, "type": "dir", "children": []}
    state["count"] += 1

    if depth >= max_depth:
        return node

    children: list[dict[str, Any]] = []
    try:
        entries = list(os.scandir(current))
    except (OSError, PermissionError):
        node["children"] = children
        return node

    def sort_key(entry: os.DirEntry[str]) -> tuple[int, str]:
        is_dir = entry.is_dir(follow_symlinks=False)
        return (0 if is_dir else 1, entry.name.lower())

    for entry in sorted(entries, key=sort_key):
        if state["count"] >= max_entries:
            break
        if _is_hidden_name(entry.name):
            continue
        if entry.is_symlink():
            continue

        entry_path = Path(entry.path)
        if not _is_within_root(entry_path, root):
            continue

        if entry.is_dir(follow_symlinks=False):
            child = _build_dir(entry_path, root, depth + 1, state, max_depth, max_entries)
            if child is not None:
                children.append(child)
            continue

        if entry.is_file(follow_symlinks=False):
            children.append({"name": entry.name, "type": "file"})
            state["count"] += 1
            continue

    node["children"] = children
    return node


def build_project_tree(
    root: str | os.PathLike[str] | Path | None = None,
    *,
    max_depth: int = DEFAULT_MAX_DEPTH,
    max_entries: int = DEFAULT_MAX_ENTRIES,
) -> dict[str, Any]:
    """Build a safe tree representation of the repository."""

    repo_root = Path(root or Path.cwd()).resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        raise FileNotFoundError(f"Repository root does not exist: {repo_root}")

    state = {"count": 0}
    tree = _build_dir(repo_root, repo_root, 0, state, max_depth, max_entries)
    if tree is None:
        return {"name": repo_root.name, "type": "dir", "children": []}
    return tree
