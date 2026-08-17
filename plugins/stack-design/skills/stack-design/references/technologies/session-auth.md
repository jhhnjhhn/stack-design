{
  "name": "Server-side sessions",
  "category": "auth",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html"
  ],
  "license": "Open standard pattern",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "simple revocation",
    "good browser security boundary"
  ],
  "weaknesses": [
    "shared state for multiple instances",
    "CSRF protection required"
  ],
  "prefer_when": [
    "first-party browser app",
    "server controls UI and API"
  ],
  "avoid_when": [
    "delegated identity between organizations",
    "offline third-party API clients"
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
