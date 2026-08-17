# ADR-002: Load only relevant decision knowledge

## Status

Accepted

## Context

Loading every project, category, domain, and technology profile would consume agent context and dilute the decision.

## Decision

Keep workflow and routing in `SKILL.md`; load one project profile, affected categories, applicable domains, and only credible technology candidates.

## Consequences

Catalog growth does not increase routine context cost. Routing and reference integrity require automated checks.

## Review trigger

Review if agents repeatedly miss required profiles despite correct trigger metadata.
