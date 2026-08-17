{
  "name": "OpenID Connect",
  "category": "auth",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://openid.net/developers/how-connect-works/"
  ],
  "license": "Open standard",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "standard identity federation",
    "enterprise SSO interoperability"
  ],
  "weaknesses": [
    "provider and claim complexity",
    "token validation must be exact"
  ],
  "prefer_when": [
    "enterprise SSO",
    "external identity provider"
  ],
  "avoid_when": [
    "single local account system",
    "team cannot operate identity flows"
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
