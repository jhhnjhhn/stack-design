{
  "name": "Amazon SQS",
  "category": "queue",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html"
  ],
  "license": "Proprietary service",
  "vendor_lock_in": "high",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "high",
  "strengths": [
    "managed durable queue",
    "scales without broker operations"
  ],
  "weaknesses": [
    "AWS lock-in",
    "delivery and ordering semantics must fit"
  ],
  "prefer_when": [
    "AWS deployment",
    "ordinary durable asynchronous jobs"
  ],
  "avoid_when": [
    "self-hosting",
    "replayable event log is required"
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
