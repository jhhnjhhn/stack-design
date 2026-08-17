---
name: stack-design
description: Make senior-level, constraint-first technology decisions for modern application projects. Use when Codex needs to choose, compare, explain, review, or migrate an application technology stack; analyze an existing repository before adding technology; detect overengineering; produce a stack recommendation or ADR; or answer requests such as /stack-design, stack design, tech stack selection, framework comparison, architecture choice, existing-stack review, and migration advice.
---

# Stack Design

Choose the simplest stack that satisfies the real constraints.

## Workflow

1. Determine the mode: `quick`, `compare`, `existing`, `migrate`, `adr`, or the default full recommendation.
2. For an existing repository, run `python scripts/detect_stack.py [repo]` and verify important detections in manifests. Preserve the current stack unless a demonstrated problem justifies change.
3. Build the project context: stage, greenfield status, team skills, product capabilities, expected scale, deployment, budget/deadline/compliance, and existing assets.
4. Separate hard constraints from preferences. A hard constraint excludes candidates; scoring never overrides it.
5. Ask only about a critical unknown that would change the technology route (required language, private/on-prem deployment, SEO, mobile, ultra-low latency, or regulation). Otherwise state a conservative assumption and reduce confidence.
6. Read `references/principles.md` and the one matching file in `references/project-types/`. Read only the relevant files in `references/categories/`, then only the candidate profiles in `references/technologies/`. Read `references/domains/` only for regulated or domain-specific work.
7. Compare at least two credible candidates per important contested decision using `references/scoring.md`. Prefer fewer components and the team's existing assets when candidates both satisfy requirements.
8. Run the checks in `references/overengineering.md`. Do not add Redis, Kafka, Kubernetes, Elasticsearch, GraphQL, microservices, a vector database, or a second primary database without an explicit requirement that justifies it.
9. Give every selected layer a reason, evidence, and derived `low`/`medium`/`high` confidence. Use the factor rubric in `references/scoring.md`; do not invent percentages. Explain meaningful rejected alternatives. Include risks, assumptions, measurable scaling triggers, and an exit or migration path.
10. Save an ADR only when requested, using `templates/adr.md`. For migration requests, read `references/migration.md` and use `templates/migration-report.md`.
11. When saving a decision, create a structured JSON recommendation from `templates/recommendation.json`, run `python scripts/self_check.py <report.json>`, then render Markdown with `python scripts/render_report.py <report.json> <report.md>`. Resolve failures and explain intentional warnings. For chat-only output, follow the same fields and apply the checks manually.

## Reference routing

- Always read: `references/principles.md`.
- Scoring or comparisons: `references/scoring.md`, `scripts/confidence.py`, and `templates/comparison.md`.
- AI-maintainability decision: `references/ai-coding-compatibility.md`.
- New project: one `references/project-types/*.md` file plus affected category files.
- Existing project: detector output, relevant manifests, then affected category files.
- Migration: `references/migration.md`.
- Payment, health, enterprise identity, or game workloads: matching `references/domains/*.md`.
- Technology facts: read only the profiles for real candidates, never the entire directory.

## Decision priority

Apply this order: hard constraints > organization constraints > existing assets > product requirements > team fit > lifecycle cost > technical performance > popularity or novelty.

Default to a modular monolith. Introduce scale technology only after a current requirement or measurable trigger establishes its value.

## Output

Use `templates/recommendation.json` as the source of truth and `templates/recommendation.schema.json` as its contract. Render the default readable report with `scripts/render_report.py`. Include:

- Context and hard constraints
- Architecture shape
- A table with layer, choice, derived confidence, evidence, and reason
- Alternatives and rejected technologies with reasons
- Overengineering check
- Risks and assumptions
- Scaling triggers and evolution path
- ADR summary

For `quick`, give stack, short rationale, and avoided technologies. For `compare`, include a dimension table and a prose best-fit conclusion. For `existing`, report detected stack and label choices `KEEP`, `ADD`, `REPLACE`, or `REMOVE`. For `migrate`, conclude `KEEP`, `MIGRATE`, or `PARTIAL`.

Do not invent precise load thresholds. When evidence is missing, phrase triggers as measurable conditions or label any numeric threshold as an assumption requiring load testing.
