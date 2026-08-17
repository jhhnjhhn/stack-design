{
  "name": "Server-Sent Events",
  "category": "realtime",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://html.spec.whatwg.org/multipage/server-sent-events.html"
  ],
  "license": "Open standard",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "simple server-to-client stream",
    "browser reconnection support"
  ],
  "weaknesses": [
    "one-way communication",
    "connection limits need planning"
  ],
  "prefer_when": [
    "notifications or token streams",
    "server-to-client updates"
  ],
  "avoid_when": [
    "bidirectional low-latency protocol",
    "binary messages"
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
