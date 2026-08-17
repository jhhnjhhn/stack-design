{
  "name": "REST",
  "category": "api-style",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://www.rfc-editor.org/rfc/rfc9110"
  ],
  "license": "Open standard",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "broad interoperability",
    "simple HTTP tooling"
  ],
  "weaknesses": [
    "over/under-fetching in some clients",
    "conventions must be documented"
  ],
  "prefer_when": [
    "resource-oriented public or internal APIs",
    "broad client ecosystem"
  ],
  "avoid_when": [
    "streaming protocol",
    "strict low-latency service RPC"
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
