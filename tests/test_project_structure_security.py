from __future__ import annotations

import os
import sys
import tempfile
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


class ProjectStructureSecurityTests(unittest.TestCase):
    def test_sensitive_names_are_hidden(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            (repo / "token.txt").write_text("secret", encoding="utf-8")
            (repo / "secret_notes.md").write_text("secret", encoding="utf-8")
            (repo / "auth.json").write_text("secret", encoding="utf-8")
            (repo / "safe.txt").write_text("visible", encoding="utf-8")

            tree = build_project_tree(repo)
            names = [node["name"] for node in walk(tree)]

            self.assertIn("safe.txt", names)
            self.assertNotIn("token.txt", names)
            self.assertNotIn("secret_notes.md", names)
            self.assertNotIn("auth.json", names)

    @unittest.skipUnless(hasattr(os, "symlink"), "Symlinks are unavailable on this platform")
    def test_symlink_escape_is_not_revealed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, tempfile.TemporaryDirectory() as outside_dir:
            repo = Path(temp_dir)
            outside = Path(outside_dir)
            (outside / "outside.txt").write_text("outside", encoding="utf-8")
            target = repo / "outside-link"

            try:
                os.symlink(outside, target, target_is_directory=True)
            except OSError:
                self.skipTest("Symlink creation is not permitted in this environment")

            tree = build_project_tree(repo)
            names = [node["name"] for node in walk(tree)]
            self.assertNotIn("outside-link", names)
            self.assertNotIn("outside.txt", names)

    def test_file_contents_are_never_returned(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            (repo / "data.txt").write_text("super secret content", encoding="utf-8")
            tree = build_project_tree(repo)
            for node in walk(tree):
                self.assertEqual(set(node.keys()), {"name", "type"} | ({"children"} if node["type"] == "dir" else set()))
                self.assertNotIn("content", node)
                self.assertNotIn("data", node)


if __name__ == "__main__":
    unittest.main()
