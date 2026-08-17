{
  "name": "Cloudflare R2",
  "category": "object-storage",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://developers.cloudflare.com/r2/"
  ],
  "license": "Proprietary service",
  "vendor_lock_in": "high",
  "operational_complexity": "low",
  "breaking_change_risk": "low",
  "exit_cost": "high",
  "strengths": [
    "S3-compatible API",
    "egress model can suit edge delivery"
  ],
  "weaknesses": [
    "managed vendor dependency",
    "feature differences from S3"
  ],
  "prefer_when": [
    "Cloudflare delivery stack",
    "egress-sensitive public assets"
  ],
  "avoid_when": [
    "private deployment",
    "AWS-native integrations dominate"
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
