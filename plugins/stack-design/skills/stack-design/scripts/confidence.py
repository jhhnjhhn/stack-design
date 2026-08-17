#!/usr/bin/env python3
"""Deterministically derive confidence from evidence completeness factors."""

from __future__ import annotations

import argparse
import json


REQUIRED = ("requirements", "constraints", "profile_quality", "candidate_gap")


def confidence_level(factors: dict[str, int | None]) -> str:
    values = [factors.get(key) for key in REQUIRED]
    if any(value not in (0, 1, 2) for value in values):
        raise ValueError(f"required factors must be 0, 1, or 2: {REQUIRED}")
    optional = factors.get("existing_stack")
    if optional is not None:
        if optional not in (0, 1, 2):
            raise ValueError("existing_stack must be null, 0, 1, or 2")
        values.append(optional)
    ratio = sum(values) / (2 * len(values))
    return "high" if ratio >= 0.8 else "medium" if ratio >= 0.55 else "low"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for key in REQUIRED:
        parser.add_argument(f"--{key.replace('_', '-')}", type=int, choices=(0, 1, 2), required=True)
    parser.add_argument("--existing-stack", type=int, choices=(0, 1, 2))
    args = parser.parse_args()
    factors = vars(args)
    print(json.dumps({"level": confidence_level(factors), "factors": factors}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
