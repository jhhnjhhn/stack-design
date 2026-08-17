{
  "name": "No shared cache",
  "category": "cache-strategy",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "decision strategy; version independent",
  "sources": ["https://martinfowler.com/bliki/TwoHardThings.html"],
  "license": "Pattern; not applicable",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": ["no invalidation or extra service", "database remains authoritative"],
  "weaknesses": ["cannot hide a demonstrated hot path", "repeated expensive work remains"],
  "prefer_when": ["database meets latency target", "early-stage application"],
  "avoid_when": ["measured hot keys dominate latency", "shared ephemeral coordination is required"],
  "ai_coding": {"documentation": "high", "examples": "high", "api_stability": "high", "breaking_change_risk": "low", "type_safety": "high", "error_clarity": "high", "tooling": "high", "overall": "high"}
}
