{
  "name": "Django",
  "category": "backend-framework",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "batteries-included ORM/admin/auth",
    "mature ecosystem"
  ],
  "weaknesses": [
    "heavier conventions",
    "async ecosystem is less uniform"
  ],
  "prefer_when": [
    "data-backed product with admin",
    "Python monolith"
  ],
  "avoid_when": [
    "tiny stateless API",
    "non-Python team"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "high",
    "breaking_change_risk": "low",
    "type_safety": "medium",
    "error_clarity": "high",
    "tooling": "high",
    "overall": "high"
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://docs.djangoproject.com/"
  ],
  "license": "BSD-3-Clause",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
