{
  "name": "Grafana",
  "category": "observability",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://grafana.com/docs/grafana/latest/",
    "https://grafana.com/licensing/"
  ],
  "license": "AGPL-3.0 with commercial options",
  "vendor_lock_in": "medium",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "medium",
  "strengths": [
    "broad dashboard data-source support",
    "mature visualization ecosystem"
  ],
  "weaknesses": [
    "dashboard governance and operations",
    "not a telemetry store by itself"
  ],
  "prefer_when": [
    "multiple operational data sources",
    "shared dashboards are needed"
  ],
  "avoid_when": [
    "provider dashboards already suffice",
    "no metrics ownership"
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
