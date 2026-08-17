{
  "name": "ClickHouse",
  "category": "analytics-database",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "fast columnar analytics",
    "high ingestion throughput"
  ],
  "weaknesses": [
    "additional data pipeline and operations",
    "not a transactional source of truth"
  ],
  "prefer_when": [
    "large analytical scans",
    "telemetry/event analytics"
  ],
  "avoid_when": [
    "small reporting workload",
    "OLTP is primary"
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
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://clickhouse.com/docs/"
  ],
  "license": "Apache-2.0",
  "vendor_lock_in": "low",
  "operational_complexity": "high",
  "breaking_change_risk": "low",
  "exit_cost": "low"
}
