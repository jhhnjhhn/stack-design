{
  "name": "Database-backed jobs",
  "category": "queue",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "minimal infrastructure",
    "transaction-friendly enqueue"
  ],
  "weaknesses": [
    "limited very-high-throughput behavior",
    "polling and locking need care"
  ],
  "prefer_when": [
    "modest background workload",
    "simple monolith"
  ],
  "avoid_when": [
    "massive durable event stream",
    "complex routing required"
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
    "https://www.postgresql.org/docs/current/explicit-locking.html"
  ],
  "license": "Depends on primary database",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
