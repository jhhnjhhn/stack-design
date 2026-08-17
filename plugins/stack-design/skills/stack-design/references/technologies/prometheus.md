{
  "name": "Prometheus",
  "category": "observability",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://prometheus.io/docs/introduction/overview/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "mature metrics and alerting ecosystem",
    "powerful time-series queries"
  ],
  "weaknesses": [
    "retention and HA operations",
    "cardinality requires discipline"
  ],
  "prefer_when": [
    "metrics and SLOs are operational requirements",
    "team can operate it"
  ],
  "avoid_when": [
    "logs and managed monitoring are sufficient",
    "unbounded labels"
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
