{
  "name": "Managed model API",
  "category": "ai-ml",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "provider-neutral decision profile; verify provider models",
  "sources": ["https://platform.openai.com/docs/overview"],
  "license": "Proprietary service terms",
  "vendor_lock_in": "medium",
  "operational_complexity": "low",
  "breaking_change_risk": "medium",
  "exit_cost": "medium",
  "strengths": ["fast access to managed models", "no model-serving operations"],
  "weaknesses": ["provider cost privacy and availability", "model behavior changes require evaluation"],
  "prefer_when": ["product needs model capability quickly", "data policy permits provider processing"],
  "avoid_when": ["offline or air-gapped execution", "provider terms violate compliance"],
  "ai_coding": {"documentation": "high", "examples": "high", "api_stability": "medium", "breaking_change_risk": "medium", "type_safety": "medium", "error_clarity": "medium", "tooling": "high", "overall": "high"}
}
