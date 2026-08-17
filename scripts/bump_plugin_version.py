#!/usr/bin/env python3
"""Update the Codex and Claude plugin manifests to one semantic version."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
MANIFESTS = (
    ROOT / "plugins" / "stack-design" / ".codex-plugin" / "plugin.json",
    ROOT / "plugins" / "stack-design" / ".claude-plugin" / "plugin.json",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version")
    args = parser.parse_args()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", args.version):
        parser.error("version must be semantic version syntax")
    for path in MANIFESTS:
        data = json.loads(path.read_text(encoding="utf-8"))
        data["version"] = args.version
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"updated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
