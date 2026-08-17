{
  "name": "pgvector",
  "category": "vector-search",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "vectors beside relational metadata",
    "one operational database"
  ],
  "weaknesses": [
    "specialized scale/features may be lower",
    "index tuning still required"
  ],
  "prefer_when": [
    "initial RAG on PostgreSQL",
    "moderate vector corpus"
  ],
  "avoid_when": [
    "billions of vectors or specialized distribution is proven",
    "no vector requirement"
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
    "https://github.com/pgvector/pgvector"
  ],
  "license": "PostgreSQL",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
