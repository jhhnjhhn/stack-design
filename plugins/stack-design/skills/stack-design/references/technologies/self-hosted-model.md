{
  "name": "Self-hosted model serving",
  "category": "ai-ml",
  "status": "TRIAL",
  "maturity": "medium",
  "last_reviewed": "2026-08-17",
  "source_version": "architecture profile; serving stack must be selected separately",
  "sources": ["https://docs.vllm.ai/en/latest/"],
  "license": "Depends on serving software and model",
  "vendor_lock_in": "low",
  "operational_complexity": "high",
  "breaking_change_risk": "medium",
  "exit_cost": "high",
  "strengths": ["data and serving control", "can optimize steady specialized workloads"],
  "weaknesses": ["GPU capacity reliability and model operations", "model license and security burden"],
  "prefer_when": ["privacy or offline constraints require it", "steady load justifies operations"],
  "avoid_when": ["small MVP without model operations", "managed API satisfies constraints"],
  "ai_coding": {"documentation": "medium", "examples": "medium", "api_stability": "medium", "breaking_change_risk": "medium", "type_safety": "medium", "error_clarity": "medium", "tooling": "medium", "overall": "medium"}
}
