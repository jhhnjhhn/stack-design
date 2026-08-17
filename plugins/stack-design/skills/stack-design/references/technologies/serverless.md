{
  "name": "Serverless",
  "category": "deployment",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "strengths": [
    "managed scaling",
    "low idle operations"
  ],
  "weaknesses": [
    "platform limits and lock-in",
    "cold starts and debugging variability"
  ],
  "prefer_when": [
    "bursty stateless workloads",
    "managed platform fits constraints"
  ],
  "avoid_when": [
    "steady predictable load on existing VM",
    "private isolated deployment"
  ],
  "ai_coding": {
    "documentation": "high",
    "examples": "high",
    "api_stability": "medium",
    "breaking_change_risk": "medium",
    "type_safety": "medium",
    "error_clarity": "high",
    "tooling": "high",
    "overall": "medium"
  },
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"
  ],
  "license": "Vendor service terms",
  "vendor_lock_in": "high",
  "operational_complexity": "medium",
  "breaking_change_risk": "medium",
  "exit_cost": "high"
}
