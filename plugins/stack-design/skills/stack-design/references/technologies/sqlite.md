{
  "name": "SQLite",
  "category": "database",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "zero service operations",
    "excellent embedded reliability"
  ],
  "weaknesses": [
    "single-writer/concurrency limits",
    "multi-node coordination is external"
  ],
  "prefer_when": [
    "local app",
    "low-concurrency single-node tool"
  ],
  "avoid_when": [
    "multi-node write-heavy service",
    "strict HA database requirement"
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
    "https://sqlite.org/docs.html"
  ],
  "license": "Public Domain",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
