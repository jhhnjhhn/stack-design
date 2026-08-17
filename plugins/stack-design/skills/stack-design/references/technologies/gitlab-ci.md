{
  "name": "GitLab CI/CD",
  "category": "cicd",
  "status": "ADOPT",
  "maturity": "high",
  "last_reviewed": "2026-08-17",
  "source_version": "technology-level decision profile; verify project-specific versions",
  "sources": [
    "https://docs.gitlab.com/ci/"
  ],
  "license": "MIT core / proprietary service features",
  "vendor_lock_in": "medium",
  "operational_complexity": "medium",
  "breaking_change_risk": "low",
  "exit_cost": "medium",
  "strengths": [
    "integrated GitLab pipeline and registry",
    "self-managed option"
  ],
  "weaknesses": [
    "GitLab coupling",
    "runner operations for self-hosting"
  ],
  "prefer_when": [
    "GitLab is the source platform",
    "integrated DevSecOps workflow"
  ],
  "avoid_when": [
    "repository is standardized elsewhere",
    "tiny project needs only manual deploy"
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
