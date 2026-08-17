#!/usr/bin/env python3
"""Update last_reviewed in one or more JSON technology profiles."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profiles", nargs="+")
    parser.add_argument("--reviewed", default=date.today().strftime("%Y-%m"))
    args = parser.parse_args()
    for value in args.profiles:
        path = Path(value)
        data = json.loads(path.read_text(encoding="utf-8"))
        data["last_reviewed"] = args.reviewed
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"updated {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
