{
  "name": "Alibaba Cloud OSS",
  "category": "object-storage",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://www.alibabacloud.com/help/en/oss/"
  ],
  "license": "Proprietary service",
  "vendor_lock_in": "high",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "high",
  "strengths": [
    "managed storage in Alibaba Cloud",
    "China-region ecosystem"
  ],
  "weaknesses": [
    "provider lock-in",
    "egress and API differences"
  ],
  "prefer_when": [
    "Alibaba Cloud is an organization standard",
    "China-region deployment"
  ],
  "avoid_when": [
    "cloud portability dominates",
    "self-hosting is mandatory"
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
