{
  "name": "Redis",
  "category": "cache",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "fast shared ephemeral state",
    "useful primitives for rate limits and queues"
  ],
  "weaknesses": [
    "invalidation and durability complexity",
    "another service to operate"
  ],
  "prefer_when": [
    "measured shared cache need",
    "session lock rate-limit or broker need"
  ],
  "avoid_when": [
    "database is already sufficient",
    "no explicit shared-state use"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "medium",
    "breaking_change_risk": "medium",
    "type_safety": "medium",
    "error_clarity": "high",
    "tooling": "high",
    "overall": "high"
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://redis.io/docs/latest/",
    "https://redis.io/legal/licenses/"
  ],
  "license": "RSALv2/SSPLv1/AGPLv3 depending on version",
  "vendor_lock_in": "medium",
  "operational_complexity": "medium",
  "breaking_change_risk": "medium",
  "exit_cost": "medium"
}
