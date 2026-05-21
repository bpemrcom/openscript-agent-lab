from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from project_structure.tree import build_project_tree


def walk(node):
    yield node
    for child in node.get("children", []):
        yield from walk(child)


class ProjectStructureTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = build_project_tree(ROOT)

    def test_tree_contains_readme(self) -> None:
        names = [node["name"] for node in walk(self.tree)]
        self.assertIn("README.md", names)

    def test_tree_hides_git_and_env(self) -> None:
        names = [node["name"] for node in walk(self.tree)]
        self.assertNotIn(".git", names)
        self.assertNotIn(".env", names)

    def test_tree_has_no_absolute_paths(self) -> None:
        for node in walk(self.tree):
            self.assertNotIn("path", node)
            self.assertNotIn("absolute_path", node)
            self.assertIsInstance(node["name"], str)
            self.assertNotIn(":", node["name"])

    def test_entries_use_only_safe_fields(self) -> None:
        for node in walk(self.tree):
            self.assertEqual(set(node.keys()), {"name", "type"} | ({"children"} if node["type"] == "dir" else set()))
            self.assertIn(node["type"], {"file", "dir"})


if __name__ == "__main__":
    unittest.main()
