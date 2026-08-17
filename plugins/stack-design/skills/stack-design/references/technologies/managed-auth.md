{
  "name": "Managed Auth",
  "category": "auth",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://auth0.com/docs/get-started"
  ],
  "license": "Proprietary service",
  "vendor_lock_in": "high",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "high",
  "strengths": [
    "fast secure baseline",
    "hosted identity operations"
  ],
  "weaknesses": [
    "vendor pricing and lock-in",
    "custom flows may be constrained"
  ],
  "prefer_when": [
    "speed matters and vendor fits compliance",
    "team lacks identity operations"
  ],
  "avoid_when": [
    "mandatory self-hosting",
    "exit requirements are strict"
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
