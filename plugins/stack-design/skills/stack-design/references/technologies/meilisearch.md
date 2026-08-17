{
  "name": "Meilisearch",
  "category": "search",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "developer-friendly typo-tolerant search",
    "fast product search setup"
  ],
  "weaknesses": [
    "separate index and synchronization",
    "fewer enterprise analytics features"
  ],
  "prefer_when": [
    "product search exceeds SQL FTS",
    "moderate search scale"
  ],
  "avoid_when": [
    "basic SQL search is enough",
    "complex enterprise search features"
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
    "https://www.meilisearch.com/docs"
  ],
  "license": "MIT",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "medium"
}
