{
  "name": "Qdrant",
  "category": "vector-database",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "purpose-built vector filtering",
    "self-hosted and managed options"
  ],
  "weaknesses": [
    "additional store and synchronization",
    "higher operational surface"
  ],
  "prefer_when": [
    "vector scale or features exceed pgvector",
    "vector workload is core"
  ],
  "avoid_when": [
    "early RAG fits PostgreSQL",
    "no measured vector constraint"
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
    "https://qdrant.tech/documentation/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "medium"
}
