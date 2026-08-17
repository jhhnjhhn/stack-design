{
  "name": "tRPC",
  "category": "api-style",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://trpc.io/docs"
  ],
  "license": "MIT",
  "vendor_lock_in": "medium",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "medium",
  "strengths": [
    "end-to-end TypeScript inference",
    "fast internal full-stack iteration"
  ],
  "weaknesses": [
    "tight client/server coupling",
    "weak fit for non-TypeScript consumers"
  ],
  "prefer_when": [
    "single TypeScript product boundary",
    "client and server release together"
  ],
  "avoid_when": [
    "public multi-language API",
    "independent client lifecycle"
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
