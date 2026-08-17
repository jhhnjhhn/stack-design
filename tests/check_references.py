#!/usr/bin/env python3
"""Check local Markdown links and skill-relative resource references."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "plugins" / "stack-design" / "skills" / "stack-design"
LINK = re.compile(r"\[[^]]+\]\((?!https?://|#)([^)]+)\)")
RESOURCE = re.compile(r"`((?:references|templates|scripts)/[^` ]+\.(?:md|py|json))`")


def main() -> int:
    failures = []
    for document in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in document.parts):
            continue
        text = document.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            clean = target.split("#", 1)[0]
            if clean and not (document.parent / clean).exists():
                failures.append(f"{document.relative_to(ROOT)} -> {target}")
        if document == SKILL / "SKILL.md":
            for target in RESOURCE.findall(text):
                if "*" in target:
                    exists = any(SKILL.glob(target))
                else:
                    exists = (SKILL / target).exists()
                if not exists:
                    failures.append(f"{document.relative_to(ROOT)} -> {target}")
    for failure in sorted(set(failures)):
        print(f"[FAIL] broken reference: {failure}")
    if failures:
        return 1
    print("[PASS] local Markdown and skill resource references resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
