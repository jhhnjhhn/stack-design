{
  "name": "WebSocket",
  "category": "realtime",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://websockets.spec.whatwg.org/"
  ],
  "license": "Open standard",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "bidirectional low-latency channel",
    "broad client support"
  ],
  "weaknesses": [
    "connection lifecycle and scaling complexity",
    "backpressure and recovery are application concerns"
  ],
  "prefer_when": [
    "interactive bidirectional realtime",
    "presence or collaborative state"
  ],
  "avoid_when": [
    "one-way updates fit SSE",
    "infrequent updates fit polling"
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
