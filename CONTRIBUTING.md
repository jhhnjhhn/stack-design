# Contributing

Contributions must improve a technology decision rather than advertise a tool. Explain the decision problem, affected scenarios, and introduced trade-off.

## Technology profiles

A profile must include strengths, weaknesses, selection and avoidance boundaries, maturity, lifecycle status, exact review date, version scope, HTTPS sources, license, vendor lock-in, operational complexity, exit cost, breaking-change risk, and complete AI-coding metadata. Prefer official documentation and primary specifications. Add or update at least two scenarios.

## Scenario changes

Write a concrete user prompt. Define required, forbidden, and acceptable candidates. Keep multiple valid solutions possible where the requirements permit them. When changing the evaluator, add an adversarial mutation that should fail.

## Validation

Run:

```bash
python scripts/validate_all.py
```

If plugin metadata changes, keep the Codex and Claude manifest versions synchronized with:

```bash
python scripts/bump_plugin_version.py <semver>
```

Record durable policy decisions in `docs/adr/` rather than relitigating them in profile prose.
