{
  "name": "MySQL",
  "category": "database",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "mature relational database",
    "broad managed support"
  ],
  "weaknesses": [
    "some advanced PostgreSQL features differ",
    "migration adds little when PostgreSQL exists"
  ],
  "prefer_when": [
    "existing MySQL expertise",
    "company standard"
  ],
  "avoid_when": [
    "replacement is preference-only",
    "embedded application"
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
    "https://dev.mysql.com/doc/"
  ],
  "license": "GPL-2.0 with commercial options",
  "vendor_lock_in": "medium",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "medium"
}
