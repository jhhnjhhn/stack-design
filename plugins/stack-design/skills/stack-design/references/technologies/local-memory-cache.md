{
  "name": "Local in-memory cache",
  "category": "cache-strategy",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "decision strategy; implementation specific",
  "sources": ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching"],
  "license": "Pattern; not applicable",
  "vendor_lock_in": "low",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": ["no network dependency", "simple for disposable repeated computation"],
  "weaknesses": ["not coherent across instances", "memory bounds and expiry are required"],
  "prefer_when": ["single process or stale copies are acceptable", "cache entries are disposable"],
  "avoid_when": ["shared consistency is required", "unbounded keys"],
  "ai_coding": {"documentation": "high", "examples": "high", "api_stability": "high", "breaking_change_risk": "low", "type_safety": "medium", "error_clarity": "high", "tooling": "high", "overall": "high"}
}
