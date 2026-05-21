"""Minimal stdlib HTTP server for the Stage 2 project structure viewer."""

from __future__ import annotations

import argparse
import json
from functools import partial
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from .tree import build_project_tree

STATIC_DIR = Path(__file__).resolve().parent / "static"


class ProjectStructureHandler(BaseHTTPRequestHandler):
    server_version = "OpenScriptProjectStructure/1.0"

    def _send_bytes(self, status: HTTPStatus, payload: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _send_json(self, status: HTTPStatus, data: dict[str, object]) -> None:
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self._send_bytes(status, payload, "application/json")

    def _serve_static_file(self, filename: str, content_type: str) -> None:
        file_path = STATIC_DIR / filename
        if not file_path.exists():
            self.send_error(HTTPStatus.NOT_FOUND, "Static asset not found")
            return
        payload = file_path.read_bytes()
        self._send_bytes(HTTPStatus.OK, payload, content_type)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        repo_root = getattr(self.server, "repo_root", Path.cwd())  # type: ignore[attr-defined]

        if path == "/healthz":
            self._send_json(HTTPStatus.OK, {"ok": True})
            return

        if path == "/api/project-tree":
            self._send_json(HTTPStatus.OK, build_project_tree(repo_root))
            return

        if path in {"/project-structure/", "/project-structure"}:
            self._serve_static_file("project-structure.html", "text/html")
            return

        if path == "/project-structure/project-structure.css":
            self._serve_static_file("project-structure.css", "text/css")
            return

        if path == "/project-structure/project-structure.js":
            self._serve_static_file("project-structure.js", "application/javascript")
            return

        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


class ProjectStructureHTTPServer(ThreadingHTTPServer):
    def __init__(self, server_address: tuple[str, int], RequestHandlerClass, repo_root: Path):
        super().__init__(server_address, RequestHandlerClass)
        self.repo_root = repo_root


def run_server(host: str = "127.0.0.1", port: int = 8000, root: str | Path | None = None) -> ProjectStructureHTTPServer:
    repo_root = Path(root or Path.cwd()).resolve()
    httpd = ProjectStructureHTTPServer((host, port), ProjectStructureHandler, repo_root)
    return httpd


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the safe project structure viewer server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    parser.add_argument("--root", default=str(Path.cwd()))
    args = parser.parse_args()

    server = run_server(args.host, args.port, args.root)
    try:
        print(f"Serving on http://{args.host}:{args.port}/project-structure/")
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
