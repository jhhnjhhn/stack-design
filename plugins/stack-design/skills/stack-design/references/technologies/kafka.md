{
  "name": "Kafka",
  "category": "event-stream",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "durable replayable streams",
    "high throughput and consumer groups"
  ],
  "weaknesses": [
    "substantial operational and conceptual cost",
    "poor default job queue"
  ],
  "prefer_when": [
    "replay plus multiple consumers",
    "event streaming is core at scale"
  ],
  "avoid_when": [
    "small team or low throughput",
    "ordinary background jobs"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "high",
    "breaking_change_risk": "low",
    "type_safety": "medium",
    "error_clarity": "medium",
    "tooling": "high",
    "overall": "medium"
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://kafka.apache.org/documentation/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "high",
  "breaking_change_risk": "low",
  "exit_cost": "high"
}
