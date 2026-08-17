{
  "name": "gRPC",
  "category": "api-style",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://grpc.io/docs/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "low",
  "strengths": [
    "strong generated contracts",
    "efficient service-to-service calls"
  ],
  "weaknesses": [
    "browser and debugging friction",
    "schema evolution discipline required"
  ],
  "prefer_when": [
    "controlled service-to-service APIs",
    "streaming and performance matter"
  ],
  "avoid_when": [
    "simple public browser API",
    "team lacks protobuf tooling"
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
