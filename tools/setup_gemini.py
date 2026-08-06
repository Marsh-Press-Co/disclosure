"""One-time setup: copy the Gemini key from shorts-stack/.env into this
project's .env (Marsh approved the reuse in chat, 2026-08-05), then verify it
against the API. The key value is never printed.

Usage: python tools/setup_gemini.py
"""
import json
import urllib.request
from pathlib import Path

SRC = Path(r"C:/Users/Marsh/Documents/shorts-stack/.env")
DEST = Path(__file__).resolve().parents[1] / ".env"


def main():
    var = key = None
    for line in SRC.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        for name in ("GEMINI_API_KEY", "GOOGLE_API_KEY"):
            if line.startswith(name + "=") and len(line.split("=", 1)[1].strip()) > 10:
                var = name
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break
        if key:
            break
    if not key:
        raise SystemExit("no Gemini/Google key with a value found in shorts-stack/.env")

    DEST.write_text(f"GEMINI_API_KEY={key}\n", encoding="utf-8")

    req = urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models")
    req.add_header("x-goog-api-key", key)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    models = [m["name"].split("/")[-1] for m in data.get("models", [])]
    flash = [m for m in models if "flash" in m]
    print(f"copied {var} -> Disclosure/.env ({len(key)} chars). API OK: {len(models)} models visible.")
    print("flash-family models:", ", ".join(flash[:14]))


if __name__ == "__main__":
    main()
