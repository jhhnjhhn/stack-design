# ADR-003: Separate repository, plugin, and skill roots

## Status

Accepted

## Context

The repository needs contributor tooling and multiple distribution manifests, while the installed Skill should contain only runtime instructions and resources.

## Decision

Use the repository as a marketplace root, place the distributable plugin at `plugins/stack-design`, and place the canonical Skill at `plugins/stack-design/skills/stack-design`.

## Consequences

Codex can install the plugin from the repository marketplace; Claude Code and other compatible tools can link the inner Skill directly. Tests must resolve the canonical nested path.

## Review trigger

Review if a supported host standardizes a different package layout.
