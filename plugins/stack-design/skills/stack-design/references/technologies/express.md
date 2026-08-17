{
  "name": "Express",
  "category": "backend-framework",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://expressjs.com/"
  ],
  "license": "MIT",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "minimal ubiquitous Node HTTP framework",
    "large example ecosystem"
  ],
  "weaknesses": [
    "few architectural defaults",
    "async error and middleware discipline required"
  ],
  "prefer_when": [
    "small existing Express service",
    "team wants minimal Node framework"
  ],
  "avoid_when": [
    "large new domain app needs conventions",
    "rewrite is preference-only"
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
