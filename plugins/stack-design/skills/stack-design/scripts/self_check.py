#!/usr/bin/env python3
"""Semantically validate structured recommendations; retain a Markdown legacy check."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from confidence import confidence_level


TOP_LEVEL = {"schema_version", "mode", "context", "hard_constraints", "architecture", "selected", "alternatives", "rejected", "overengineering", "risks", "assumptions", "scaling_triggers", "evolution_path"}
MODES = {"full", "quick", "compare", "existing", "migrate", "adr"}
ADVANCED = {"kubernetes", "kafka", "redis", "elasticsearch", "microservices"}


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def check_structured(data: dict, profile_dir: Path) -> tuple[list[str], list[str], list[str]]:
    passed: list[str] = []
    warnings: list[str] = []
    failures: list[str] = []
    missing = TOP_LEVEL - data.keys()
    if missing:
        failures.append("Missing top-level fields: " + ", ".join(sorted(missing)))
        return passed, warnings, failures
    if data.get("schema_version") != "1.0":
        failures.append("schema_version must be 1.0")
    if data.get("mode") not in MODES:
        failures.append("invalid mode")
    context = data.get("context")
    if not isinstance(context, dict) or not context.get("summary"):
        failures.append("context.summary is required")
        context = {}
    for field in ("hard_constraints", "alternatives", "rejected", "overengineering", "risks", "assumptions", "scaling_triggers", "evolution_path"):
        if not isinstance(data.get(field), list):
            failures.append(f"{field} must be a list")
    architecture = data.get("architecture")
    if not isinstance(architecture, dict) or not architecture.get("choice") or not architecture.get("reason"):
        failures.append("architecture requires choice and reason")

    selected = data.get("selected")
    if not isinstance(selected, list) or not selected:
        failures.append("selected must be a non-empty list")
        selected = []
    selected_slugs = set()
    for index, item in enumerate(selected):
        label = f"selected[{index}]"
        if not isinstance(item, dict):
            failures.append(f"{label} must be an object")
            continue
        for field in ("layer", "technology", "profile", "reason", "evidence", "confidence"):
            if not item.get(field):
                failures.append(f"{label}.{field} is required")
        slug = item.get("profile", "")
        selected_slugs.add(slug)
        if slug and not (profile_dir / f"{slug}.md").is_file():
            failures.append(f"{label}.profile does not exist: {slug}")
        if not isinstance(item.get("evidence"), list) or not item.get("evidence"):
            failures.append(f"{label}.evidence must be non-empty")
        confidence = item.get("confidence", {})
        if not isinstance(confidence, dict):
            failures.append(f"{label}.confidence must be an object")
            continue
        factors = confidence.get("factors", {})
        try:
            expected = confidence_level(factors)
            if confidence.get("level") != expected:
                failures.append(f"{label}.confidence.level must be {expected} for its factors")
        except (TypeError, ValueError) as exc:
            failures.append(f"{label}.confidence factors invalid: {exc}")
        if not isinstance(confidence.get("basis"), list) or not confidence.get("basis"):
            failures.append(f"{label}.confidence.basis must be non-empty")

    req = context.get("requirements", {}) if isinstance(context.get("requirements"), dict) else {}
    deploy = context.get("deployment", {}) if isinstance(context.get("deployment"), dict) else {}
    team_size = context.get("team_size")
    if "kubernetes" in selected_slugs and (deploy.get("single_server") or (isinstance(team_size, int) and team_size < 5)) and not deploy.get("multi_node_ha"):
        failures.append("Kubernetes is not justified for a small/single-server context without multi-node HA")
    if "microservices" in selected_slugs and isinstance(team_size, int) and team_size < 5 and not req.get("independent_deploy"):
        failures.append("Microservices require independent deployment/ownership evidence for a small team")
    if "kafka" in selected_slugs and not any(req.get(key) for key in ("event_replay", "multiple_consumer_groups", "event_sourcing", "durable_high_throughput_stream")):
        failures.append("Kafka lacks an explicit streaming requirement")
    if "redis" in selected_slugs and not any(req.get(key) for key in ("shared_session", "rate_limit", "distributed_lock", "queue_broker", "measured_hot_keys")):
        failures.append("Redis lacks an explicit shared-state, broker, or measured-cache requirement")
    if "elasticsearch" in selected_slugs and not req.get("advanced_search_beyond_sql"):
        failures.append("Elasticsearch lacks evidence that SQL search is insufficient")
    rejected = {normalized(str(item.get("technology", ""))) for item in data.get("rejected", []) if isinstance(item, dict)}
    for slug in ADVANCED - selected_slugs:
        if slug not in rejected:
            warnings.append(f"Advanced alternative not explicitly rejected: {slug}")
    if not failures:
        passed.extend(["Structured contract", "Profile references", "Confidence derivation", "Overengineering guardrails"])
    return passed, warnings, failures


MARKDOWN_CHECKS = {
    "Requirements summarized": ("context",), "Constraints identified": ("hard constraints", "constraints"),
    "Alternatives included": ("alternatives considered", "alternatives"), "Rejected options explained": ("rejected technologies", "rejected"),
    "Confidence included": ("confidence",), "Risks included": ("risks",), "Assumptions included": ("assumptions",),
    "Evolution triggers included": ("scaling triggers", "review trigger"),
}


def check_markdown(text: str) -> tuple[list[str], list[str], list[str]]:
    lower = text.lower()
    passed, warnings, failures = [], ["Markdown-only validation is lexical; prefer a JSON recommendation sidecar"], []
    for label, terms in MARKDOWN_CHECKS.items():
        (passed if any(term in lower for term in terms) else failures).append(label)
    return passed, warnings, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report")
    args = parser.parse_args()
    path = Path(args.report)
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        profile_dir = Path(__file__).parents[1] / "references" / "technologies"
        passed, warnings, failures = check_structured(data, profile_dir)
    else:
        passed, warnings, failures = check_markdown(path.read_text(encoding="utf-8"))
    for item in passed:
        print(f"[PASS] {item}")
    for item in warnings:
        print(f"[WARN] {item}")
    for item in failures:
        print(f"[FAIL] {item}")
    print(f"Summary: {len(passed)} pass, {len(warnings)} warn, {len(failures)} fail")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
