{
  "name": "Microservices",
  "category": "architecture",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "architecture pattern; version independent",
  "sources": ["https://martinfowler.com/articles/microservices.html"],
  "license": "Pattern; not applicable",
  "vendor_lock_in": "low",
  "operational_complexity": "high",
  "breaking_change_risk": "low",
  "exit_cost": "high",
  "strengths": ["independent ownership deployment and scaling", "fault and lifecycle isolation"],
  "weaknesses": ["distributed data and operations complexity", "network and contract failure modes"],
  "prefer_when": ["clear organization boundaries", "independent deployment or scaling is required"],
  "avoid_when": ["small team", "few capabilities with one lifecycle"],
  "ai_coding": {"documentation": "high", "examples": "high", "api_stability": "high", "breaking_change_risk": "low", "type_safety": "medium", "error_clarity": "medium", "tooling": "high", "overall": "medium"}
}
