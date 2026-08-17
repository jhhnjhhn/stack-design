#!/usr/bin/env python3
"""Adversarial unit test for the scenario evaluator itself."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from evaluate_scenarios import evaluate_case, evaluate_directory


ROOT = Path(__file__).parents[1]


def response_for(case: dict) -> dict:
    selected_profiles = set(case["must_recommend"])
    requirements = {
        "event_replay": "kafka" in selected_profiles,
        "queue_broker": "redis" in selected_profiles,
        "advanced_search_beyond_sql": "elasticsearch" in selected_profiles,
        "independent_deploy": "microservices" in selected_profiles,
    }
    selected = [
        {
            "layer": "test", "technology": slug, "profile": slug, "reason": "Scenario requirement",
            "evidence": [case["prompt"]],
            "confidence": {"level": "high", "factors": {"requirements": 2, "constraints": 2, "profile_quality": 2, "candidate_gap": 2, "existing_stack": None}, "basis": ["Required by the scenario contract."]},
        }
        for slug in case["must_recommend"]
    ]
    rejected = [{"profile": slug, "technology": slug, "reason": "Forbidden by the scenario contract."} for slug in case["must_not_recommend"]]
    return {
        "schema_version": "1.0", "mode": "full",
        "context": {"summary": case["prompt"], "stage": "mvp", "greenfield": True, "team_size": 10, "deployment": {"single_server": False, "multi_node_ha": "kubernetes" in selected_profiles}, "requirements": requirements, "existing_stack": {}},
        "hard_constraints": [], "architecture": {"choice": "scenario-fit", "reason": "Selected from the supplied constraints."}, "selected": selected,
        "alternatives": [{"choice": "alternative"}], "rejected": rejected, "overengineering": [], "risks": [], "assumptions": [],
        "scaling_triggers": [], "evolution_path": [{"phase": "current", "changes": ["Use the selected stack."]}],
    }


def main() -> int:
    cases = json.loads((ROOT / "tests" / "scenarios" / "scenarios.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        response_dir = Path(tmp)
        for case in cases:
            (response_dir / f"{case['scenario']}.json").write_text(json.dumps(response_for(case)), encoding="utf-8")
        assert not evaluate_directory(response_dir, cases)
        mutated = response_for(cases[0])
        forbidden = cases[0]["must_not_recommend"][0]
        mutated["selected"].append({"profile": forbidden})
        assert any("must not recommend" in error for error in evaluate_case(cases[0], mutated))
    print("[PASS] evaluator accepts valid outputs and rejects an adversarial forbidden recommendation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
