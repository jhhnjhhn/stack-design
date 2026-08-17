#!/usr/bin/env python3
"""Validate executable scenario definitions and their profile references."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "plugins" / "stack-design" / "skills" / "stack-design"


def main() -> int:
    cases = json.loads((ROOT / "tests" / "scenarios" / "scenarios.json").read_text(encoding="utf-8"))
    profiles = {p.stem for p in (SKILL / "references" / "technologies").glob("*.md")}
    failures = []
    names = set()
    for case in cases:
        name = case.get("scenario")
        if not name or name in names:
            failures.append(f"invalid or duplicate scenario name: {name!r}")
        names.add(name)
        if not isinstance(case.get("prompt"), str) or len(case["prompt"].split()) < 5:
            failures.append(f"{name}: prompt is missing or not concrete")
        required = set(case.get("must_recommend", []))
        rejected = set(case.get("must_not_recommend", []))
        acceptable = set(case.get("acceptable", []))
        if required & rejected or acceptable & rejected:
            failures.append(f"{name}: technology is both allowed and rejected")
        unknown = (required | rejected | acceptable) - profiles
        if unknown:
            failures.append(f"{name}: unknown profiles {sorted(unknown)}")
        if not required:
            failures.append(f"{name}: must_recommend is empty")
        expected_sections = {"context", "hard_constraints", "architecture", "selected", "rejected", "risks", "assumptions", "scaling_triggers"}
        if not expected_sections.issubset(set(case.get("required_sections", []))):
            failures.append(f"{name}: required_sections does not cover the decision contract")
    if len(cases) < 30:
        failures.append(f"only {len(cases)} scenarios; at least 30 required")
    for failure in failures:
        print(f"[FAIL] {failure}")
    if failures:
        return 1
    print(f"[PASS] {len(cases)} executable scenario definitions are valid and reference known technologies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
