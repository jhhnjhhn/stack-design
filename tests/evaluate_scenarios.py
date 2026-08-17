#!/usr/bin/env python3
"""Evaluate structured agent outputs against scenario requirements.

Use --responses for outputs produced by any agent. With --runner, invoke a local
runner executable once per scenario as: RUNNER prompt.txt response.json SKILL_DIR.
The runner contract keeps this evaluator independent of a model vendor.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "plugins" / "stack-design" / "skills" / "stack-design"
sys.path.insert(0, str(SKILL / "scripts"))

from self_check import check_structured  # noqa: E402


def evaluate_case(case: dict, response: dict) -> list[str]:
    errors = []
    for section in case["required_sections"]:
        if section not in response:
            errors.append(f"missing section: {section}")
    selected = {item.get("profile") for item in response.get("selected", []) if isinstance(item, dict)}
    rejected = {item.get("profile", item.get("technology", "")).lower().replace(" ", "-") for item in response.get("rejected", []) if isinstance(item, dict)}
    for profile in case["must_recommend"]:
        if profile not in selected:
            errors.append(f"must recommend: {profile}")
    for profile in case["must_not_recommend"]:
        if profile in selected:
            errors.append(f"must not recommend: {profile}")
        if profile not in rejected:
            errors.append(f"must explicitly reject: {profile}")
    if not response.get("alternatives"):
        errors.append("alternatives must be non-empty")
    if not response.get("evolution_path"):
        errors.append("evolution_path must be non-empty")
    _, _, semantic_failures = check_structured(response, SKILL / "references" / "technologies")
    errors.extend(f"semantic self-check: {failure}" for failure in semantic_failures)
    return errors


def evaluate_directory(response_dir: Path, cases: list[dict]) -> list[str]:
    failures = []
    for case in cases:
        path = response_dir / f"{case['scenario']}.json"
        if not path.is_file():
            failures.append(f"{case['scenario']}: response file missing")
            continue
        try:
            response = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{case['scenario']}: invalid JSON: {exc}")
            continue
        failures.extend(f"{case['scenario']}: {error}" for error in evaluate_case(case, response))
    return failures


def run_agent(runner: Path, response_dir: Path, cases: list[dict]) -> None:
    response_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        prompt_dir = Path(tmp)
        for case in cases:
            prompt_path = prompt_dir / f"{case['scenario']}.txt"
            output_path = response_dir / f"{case['scenario']}.json"
            prompt_path.write_text(case["prompt"] + "\nReturn the structured recommendation JSON contract only.\n", encoding="utf-8")
            result = subprocess.run([str(runner), str(prompt_path), str(output_path), str(SKILL)], check=False)
            if result.returncode:
                raise RuntimeError(f"runner failed for {case['scenario']} with exit code {result.returncode}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--responses", type=Path, required=True)
    parser.add_argument("--runner", type=Path, help="optional executable implementing the documented runner contract")
    args = parser.parse_args()
    cases = json.loads((ROOT / "tests" / "scenarios" / "scenarios.json").read_text(encoding="utf-8"))
    if args.runner:
        run_agent(args.runner.resolve(), args.responses, cases)
    failures = evaluate_directory(args.responses, cases)
    for failure in failures:
        print(f"[FAIL] {failure}")
    if failures:
        print(f"Scenario evaluation failed with {len(failures)} issue(s).")
        return 1
    print(f"[PASS] {len(cases)} agent responses satisfy their scenario contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
