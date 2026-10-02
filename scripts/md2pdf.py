#!/usr/bin/env python3
"""Turn a Markdown report, quiz or answer key into a printable A4 PDF.

Usage: python3 scripts/md2pdf.py <in.md> <out.pdf>

Needs the `markdown` package (pip install markdown) and Google Chrome or Chromium.
Set CHROME to the browser binary if it is not found automatically.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import time
from html import escape
from pathlib import Path

import markdown

CSS = """
@page { size: A4; margin: 16mm 15mm; }
body { font-family: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif; font-size: 11pt; line-height: 1.45; color: #20201f; }
h1 { font-size: 20pt; margin: 0 0 4pt; }
h2 { font-size: 13.5pt; margin: 16pt 0 6pt; border-bottom: 2px solid #20201f; padding-bottom: 2pt; }
h3 { font-size: 11.5pt; margin: 12pt 0 4pt; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 10pt; }
th, td { border: 1px solid #6d6b67; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #edece8; }
code { font-family: "SF Mono", Menlo, monospace; font-size: 9.5pt; }
blockquote { margin: 6pt 0; padding: 4pt 10pt; border-left: 4px solid #d97757; background: #f6f6f4; }
.answer { border-bottom: 1px solid #6d6b67; height: 18pt; }
li { margin: 2pt 0; }
"""

CANDIDATES = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome", "chromium", "chromium-browser",
]


def find_chrome() -> str:
    for c in CANDIDATES:
        if c and (Path(c).exists() or shutil.which(c)):
            return c
    sys.exit("md2pdf: Chrome or Chromium not found, set CHROME=/path/to/browser")


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out = Path(sys.argv[1]), Path(sys.argv[2]).resolve()
    text = src.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "sane_lists"])
    # The first heading becomes the PDF's title, instead of the temporary file name
    title = next((line.lstrip("# ").strip() for line in text.splitlines() if line.startswith("# ")), src.stem)
    html = (f"<!doctype html><html><head><meta charset='utf-8'><title>{escape(title)}</title>"
            f"<style>{CSS}</style></head><body>{body}</body></html>")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    out.unlink(missing_ok=True)
    # A throwaway profile, so a running Chrome window cannot block the headless one
    profile = tempfile.mkdtemp(prefix="md2pdf-")
    try:
        with tempfile.TemporaryFile() as log:
            proc = subprocess.Popen([find_chrome(), "--headless=new", "--no-first-run", "--disable-gpu",
                                     "--no-pdf-header-footer", f"--user-data-dir={profile}",
                                     f"--print-to-pdf={out}", Path(f.name).as_uri()], stdout=log, stderr=log)
            # On macOS headless Chrome often writes the file and then never exits,
            # so wait for its "bytes written" line and stop it ourselves.
            deadline = time.time() + 60
            while time.time() < deadline and proc.poll() is None:
                log.seek(0)
                if b"bytes written to file" in log.read():
                    break
                time.sleep(0.3)
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
    finally:
        os.unlink(f.name)
        shutil.rmtree(profile, ignore_errors=True)
    if not out.is_file():
        sys.exit("md2pdf: no PDF was written")
    print(out)


if __name__ == "__main__":
    main()
