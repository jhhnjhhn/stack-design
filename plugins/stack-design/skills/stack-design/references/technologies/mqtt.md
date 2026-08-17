{
  "name": "MQTT",
  "category": "realtime",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://mqtt.org/mqtt-specification/"
  ],
  "license": "Open standard",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "lightweight pub/sub protocol",
    "suited to constrained devices"
  ],
  "weaknesses": [
    "broker operations",
    "web product semantics need adaptation"
  ],
  "prefer_when": [
    "IoT devices",
    "intermittent constrained networks"
  ],
  "avoid_when": [
    "ordinary browser application",
    "REST is sufficient"
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
