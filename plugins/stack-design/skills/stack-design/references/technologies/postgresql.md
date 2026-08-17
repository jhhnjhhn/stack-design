{
  "name": "PostgreSQL",
  "category": "database",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "transactions and relational integrity",
    "JSON FTS and vector extensions"
  ],
  "weaknesses": [
    "horizontal write scaling needs planning",
    "requires database operations"
  ],
  "prefer_when": [
    "most relational applications",
    "one versatile primary store"
  ],
  "avoid_when": [
    "embedded offline-only app",
    "specialized analytics dominates"
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
    "https://www.postgresql.org/docs/"
  ],
  "license": "PostgreSQL",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
