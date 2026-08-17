{
  "name": "HTTP Polling",
  "category": "realtime",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://developer.mozilla.org/en-US/docs/Web/HTTP"
  ],
  "license": "Open standard",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "simple HTTP semantics",
    "works through common infrastructure"
  ],
  "weaknesses": [
    "wasted requests at high frequency",
    "update latency"
  ],
  "prefer_when": [
    "infrequent updates",
    "small concurrency"
  ],
  "avoid_when": [
    "sub-second bidirectional interaction",
    "very high fan-out"
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
