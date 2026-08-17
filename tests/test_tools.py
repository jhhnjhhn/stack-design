#!/usr/bin/env python3
"""Dependency-free smoke tests for monorepo detection and semantic guardrails."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "plugins" / "stack-design" / "skills" / "stack-design"
sys.path.insert(0, str(SKILL / "scripts"))

from detect_stack import detect  # noqa: E402
from self_check import check_structured  # noqa: E402


def names(result: dict, layer: str) -> set[str]:
    return {item["technology"] for item in result.get(layer, [])}


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp)
        app = repo / "apps" / "web"
        app.mkdir(parents=True)
        (app / "package.json").write_text(json.dumps({"dependencies": {"react": "19", "vite": "7", "@nestjs/core": "11", "pg": "8"}}), encoding="utf-8")
        infra = repo / "infra"
        infra.mkdir()
        (infra / "main.tf").write_text('resource "aws_s3_bucket" "assets" {}\n', encoding="utf-8")
        workflow = repo / ".github" / "workflows"
        workflow.mkdir(parents=True)
        (workflow / "ci.yml").write_text("name: CI\n", encoding="utf-8")
        result = detect(repo)
        assert names(result, "frontend") == {"React"}
        assert names(result, "backend") == {"NestJS"}
        assert names(result, "database") == {"PostgreSQL"}
        assert "Terraform" in names(result, "infrastructure")
        assert "AWS" in names(result, "cloud")
        assert "GitHub Actions" in names(result, "cicd")
        assert result["frontend"][0]["evidence"] == ["apps/web/package.json"]

    unsafe = {
        "schema_version": "1.0", "mode": "full",
        "context": {"summary": "Tiny app", "stage": "mvp", "greenfield": True, "team_size": 3, "deployment": {"single_server": True, "multi_node_ha": False}, "requirements": {}, "existing_stack": {}},
        "hard_constraints": [], "architecture": {"choice": "microservices", "reason": "Future scale"},
        "selected": [{"layer": "deploy", "technology": "Kubernetes", "profile": "kubernetes", "reason": "Future scale", "evidence": ["Maybe later"], "confidence": {"level": "low", "factors": {"requirements": 0, "constraints": 0, "profile_quality": 2, "candidate_gap": 0, "existing_stack": None}, "basis": ["Weak evidence"]}}],
        "alternatives": [], "rejected": [], "overengineering": [], "risks": [], "assumptions": [], "scaling_triggers": [], "evolution_path": [{}],
    }
    _, _, failures = check_structured(unsafe, SKILL / "references" / "technologies")
    assert any("Kubernetes" in item for item in failures)
    print("[PASS] monorepo detector and structured overengineering guardrails passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
