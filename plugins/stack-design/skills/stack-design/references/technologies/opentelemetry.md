{
  "name": "OpenTelemetry",
  "category": "observability",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://opentelemetry.io/docs/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "vendor-neutral telemetry APIs",
    "broad tracing metrics and logs ecosystem"
  ],
  "weaknesses": [
    "instrumentation and collector complexity",
    "does not provide storage or UI"
  ],
  "prefer_when": [
    "telemetry portability matters",
    "distributed diagnosis is required"
  ],
  "avoid_when": [
    "structured logs are currently sufficient",
    "no owner for telemetry"
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
