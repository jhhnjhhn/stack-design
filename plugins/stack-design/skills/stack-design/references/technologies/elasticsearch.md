{
  "name": "Elasticsearch",
  "category": "search",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "advanced relevance and aggregations",
    "large search ecosystem"
  ],
  "weaknesses": [
    "cluster cost and tuning",
    "index consistency complexity"
  ],
  "prefer_when": [
    "advanced search or analytics is proven",
    "team can operate it"
  ],
  "avoid_when": [
    "small dataset fits PostgreSQL FTS",
    "added speculatively"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "medium",
    "breaking_change_risk": "medium",
    "type_safety": "medium",
    "error_clarity": "medium",
    "tooling": "high",
    "overall": "medium"
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://www.elastic.co/guide/index.html",
    "https://www.elastic.co/pricing/faq/licensing"
  ],
  "license": "Elastic License 2.0 / AGPLv3 for selected source code",
  "vendor_lock_in": "medium",
  "operational_complexity": "high",
  "breaking_change_risk": "medium",
  "exit_cost": "medium"
}
