{
  "name": "RabbitMQ",
  "category": "message-broker",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "reliable routing and acknowledgements",
    "mature protocols"
  ],
  "weaknesses": [
    "broker operations",
    "not a replayable event log"
  ],
  "prefer_when": [
    "complex routing or reliable work queues",
    "multiple services need messaging"
  ],
  "avoid_when": [
    "simple background jobs",
    "event replay is required"
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
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://www.rabbitmq.com/docs"
  ],
  "license": "MPL-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "high",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
