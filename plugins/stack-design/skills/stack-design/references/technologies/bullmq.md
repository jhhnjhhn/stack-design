{
  "name": "BullMQ",
  "category": "queue",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "strong Node/TypeScript job API",
    "retries and scheduling"
  ],
  "weaknesses": [
    "requires Redis",
    "Redis durability semantics must fit"
  ],
  "prefer_when": [
    "Node team with worker jobs",
    "Redis already justified as broker"
  ],
  "avoid_when": [
    "no Redis justification",
    "cross-language durable messaging"
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
    "https://docs.bullmq.io/"
  ],
  "license": "MIT",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "medium"
}
