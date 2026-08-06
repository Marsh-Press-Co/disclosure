"""Regenerate graphify-out/.graphify_detect.json for the current corpus.
(Not persistent/committed - required before any graphify extract/build step.
Written via Python, never shell redirect - Windows encoding gotcha.)
"""
import json
from pathlib import Path

from graphify.detect import detect

ROOT = Path(__file__).resolve().parents[1]
result = detect(ROOT / "corpus")
(ROOT / "graphify-out" / ".graphify_detect.json").write_text(
    json.dumps(result, ensure_ascii=False), encoding="utf-8"
)
print(f"detect: {result.get('total_files')} files, {result.get('total_words'):,} words")
