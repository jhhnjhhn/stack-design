{
  "name": "Docker Compose",
  "category": "deployment",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "simple multi-container deployment",
    "portable local/VM workflow"
  ],
  "weaknesses": [
    "not a multi-node orchestrator",
    "HA is manual"
  ],
  "prefer_when": [
    "single server",
    "small team and few services"
  ],
  "avoid_when": [
    "multi-node HA/autoscaling is required",
    "managed PaaS is simpler"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "high",
    "breaking_change_risk": "low",
    "type_safety": "medium",
    "error_clarity": "high",
    "tooling": "high",
    "overall": "high"
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://docs.docker.com/compose/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
