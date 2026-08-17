{
  "name": "Modular Monolith",
  "category": "architecture",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "architecture pattern; version independent",
  "sources": ["https://martinfowler.com/articles/modular-monolith.html"],
  "license": "Pattern; not applicable",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": ["single deployable with explicit module boundaries", "low distributed-systems overhead"],
  "weaknesses": ["boundaries require discipline", "independent scaling is limited"],
  "prefer_when": ["one team or product boundary", "independent deployment is not required"],
  "avoid_when": ["capabilities require independent ownership and release", "hard isolation boundaries exist"],
  "ai_coding": {"documentation": "high", "examples": "high", "api_stability": "high", "breaking_change_risk": "low", "type_safety": "medium", "error_clarity": "high", "tooling": "high", "overall": "high"}
}
