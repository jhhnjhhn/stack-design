{
  "name": "PostgreSQL Full Text Search",
  "category": "search",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "no separate search service",
    "transactionally close to source data"
  ],
  "weaknesses": [
    "less advanced relevance and typo tolerance",
    "database load must be measured"
  ],
  "prefer_when": [
    "initial or moderate search",
    "PostgreSQL is primary"
  ],
  "avoid_when": [
    "advanced large-scale search is proven",
    "non-PostgreSQL stack"
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
    "https://www.postgresql.org/docs/current/textsearch.html"
  ],
  "license": "PostgreSQL",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
