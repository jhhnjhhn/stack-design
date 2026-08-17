{
  "name": "MongoDB",
  "category": "database",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "flexible document model",
    "horizontal distribution options"
  ],
  "weaknesses": [
    "cross-document relational integrity is harder",
    "often unnecessary beside SQL"
  ],
  "prefer_when": [
    "document access pattern is dominant",
    "schema varies materially by record"
  ],
  "avoid_when": [
    "transactional relations dominate",
    "added only for JSON"
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
    "https://www.mongodb.com/docs/",
    "https://www.mongodb.com/legal/licensing/server-side-public-license"
  ],
  "license": "SSPL-1.0 with commercial options",
  "vendor_lock_in": "medium",
  "operational_complexity": "medium",
  "breaking_change_risk": "medium",
  "exit_cost": "medium"
}
