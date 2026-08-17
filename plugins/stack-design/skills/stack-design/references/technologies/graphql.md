{
  "name": "GraphQL",
  "category": "api-style",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://graphql.org/learn/"
  ],
  "license": "Open specification",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "client-selected response shapes",
    "typed schema and tooling"
  ],
  "weaknesses": [
    "authorization caching and query-cost complexity",
    "operational surface"
  ],
  "prefer_when": [
    "multiple clients have materially different data shapes",
    "schema governance exists"
  ],
  "avoid_when": [
    "simple API with few clients",
    "REST already fits"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "high",
    "breaking_change_risk": "low",
    "type_safety": "medium",
    "error_clarity": "medium",
    "tooling": "high",
    "overall": "high"
  }
}
