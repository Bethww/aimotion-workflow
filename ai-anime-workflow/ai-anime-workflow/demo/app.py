"""Lightweight demo UI — serves a single-page interface for the workflow."""
from __future__ import annotations
import http.server
import socketserver
from pathlib import Path

PORT = 8080
DEMO_DIR = Path(__file__).parent

class DemoHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DEMO_DIR), **kwargs)

def main() -> None:
    with socketserver.TCPServer(("", PORT), DemoHandler) as httpd:
        print(f"🎬 Demo UI running at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
