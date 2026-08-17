{
  "name": "GitHub Actions",
  "category": "cicd",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://docs.github.com/actions"
  ],
  "license": "Proprietary service with reusable open components",
  "vendor_lock_in": "medium",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "medium",
  "strengths": [
    "native GitHub integration",
    "large action ecosystem"
  ],
  "weaknesses": [
    "workflow and third-party action supply-chain risk",
    "hosted runner coupling"
  ],
  "prefer_when": [
    "repository is on GitHub",
    "standard build test deploy automation"
  ],
  "avoid_when": [
    "organization mandates another CI",
    "air-gapped environment"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "high",
    "breaking_change_risk": "low",
    "type_safety": "medium",
    "error_clarity": "medium",
    "tooling": "high",
    "overall": "high"
  }
}
