#!/usr/bin/env python3
"""Validate decision profiles and decision-domain coverage."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


REQUIRED = {
    "name", "category", "status", "maturity", "last_reviewed", "source_version", "sources", "license",
    "vendor_lock_in", "operational_complexity", "breaking_change_risk", "exit_cost", "strengths", "weaknesses",
    "prefer_when", "avoid_when", "ai_coding",
}
AI_REQUIRED = {"documentation", "examples", "api_stability", "breaking_change_risk", "type_safety", "error_clarity", "tooling", "overall"}
LIFECYCLE = {"ADOPT", "TRIAL", "ASSESS", "HOLD", "AVOID"}
RATINGS = {"low", "medium", "high", "varies"}
COVERAGE = {
    "architecture": {"architecture"},
    "frontend": {"frontend-library", "frontend-framework", "frontend-build"},
    "backend": {"backend-framework", "backend-language"},
    "database": {"database", "analytics-database", "vector-search"},
    "cache": {"cache", "cache-strategy"},
    "queue": {"queue", "message-broker", "event-stream"},
    "storage": {"object-storage"},
    "search": {"search"},
    "auth": {"auth"},
    "realtime": {"realtime"},
    "api": {"api-style"},
    "ai-ml": {"ai-ml", "vector-search"},
    "devops": {"deployment", "cicd"},
    "observability": {"observability"},
}


def validate(path: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    try:
        profile = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return {}, [f"invalid JSON profile: {exc}"]
    missing = REQUIRED - profile.keys()
    if missing:
        errors.append("missing: " + ", ".join(sorted(missing)))
    for field in ("strengths", "weaknesses", "prefer_when", "avoid_when", "sources"):
        if field in profile and (not isinstance(profile[field], list) or not profile[field]):
            errors.append(f"{field} must be a non-empty list")
    if profile.get("status") not in LIFECYCLE:
        errors.append("invalid lifecycle status")
    for field in ("vendor_lock_in", "operational_complexity", "breaking_change_risk", "exit_cost"):
        if profile.get(field) not in RATINGS:
            errors.append(f"{field} must be low, medium, high, or varies")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(profile.get("last_reviewed", ""))):
        errors.append("last_reviewed must be YYYY-MM-DD")
    for source in profile.get("sources", []):
        parsed = urlparse(source)
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"source must be an absolute HTTPS URL: {source}")
    ai = profile.get("ai_coding", {})
    if not isinstance(ai, dict) or AI_REQUIRED - ai.keys():
        errors.append("ai_coding metadata is incomplete")
    elif any(value not in RATINGS for value in ai.values()):
        errors.append("ai_coding values must use rating labels")
    return profile, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default=str(Path(__file__).parents[1] / "references" / "technologies"))
    args = parser.parse_args()
    files = sorted(Path(args.directory).glob("*.md"))
    failures = 0
    profiles = []
    names = Counter()
    for path in files:
        profile, errors = validate(path)
        if profile:
            profiles.append(profile)
            names[profile.get("name")] += 1
        if errors:
            failures += 1
            print(f"[FAIL] {path.name}: {'; '.join(errors)}")
    duplicates = sorted(name for name, count in names.items() if count > 1)
    if duplicates:
        failures += 1
        print(f"[FAIL] duplicate technology names: {duplicates}")
    counts = Counter(profile.get("category") for profile in profiles)
    for decision, categories in COVERAGE.items():
        count = sum(counts[category] for category in categories)
        if count < 2:
            failures += 1
            print(f"[FAIL] {decision} has only {count} candidate profiles; at least 2 required")
    if not files:
        print("[FAIL] no profiles found")
        return 1
    if failures:
        print(f"Validated {len(files)} profiles; {failures} checks failed.")
        return 1
    print(f"[PASS] {len(files)} sourced technology profiles are complete; all {len(COVERAGE)} decision domains have candidate coverage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
