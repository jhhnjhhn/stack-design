{
  "name": "Kubernetes",
  "category": "deployment",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "standardized multi-service orchestration",
    "autoscaling and rollout controls"
  ],
  "weaknesses": [
    "large operational surface",
    "costly for small teams"
  ],
  "prefer_when": [
    "multi-node HA and many services",
    "mature platform team"
  ],
  "avoid_when": [
    "single server",
    "few services or immature DevOps"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "high",
    "breaking_change_risk": "low",
    "type_safety": "medium",
    "error_clarity": "medium",
    "tooling": "high",
    "overall": "medium"
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://kubernetes.io/docs/home/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "high",
  "breaking_change_risk": "low",
  "exit_cost": "high"
}
