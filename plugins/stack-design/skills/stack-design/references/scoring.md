# Structured scoring

Use scores as an explanation aid, never as a substitute for hard constraints.

| Dimension | Default weight | Evidence |
|---|---:|---|
| Requirement fit | 30 | Required features, latency, platform, deployment |
| Simplicity | 20 | Components, concepts, configuration, operational surface |
| Team fit | 15 | Skills, hiring, standards, training |
| Ecosystem and maturity | 10 | Stability, libraries, lifecycle |
| Maintainability | 10 | Readability, API stability, upgrades, replaceability |
| AI coding compatibility | 10 | Docs, examples, types, errors, stable patterns |
| Operational fit | 5 | Deployment, logs, scaling, backup, recovery |

Score candidates from 1–5 with one evidence sentence per dimension. Increase simplicity and time-to-market for MVPs; organization fit, compliance, and maintainability for enterprise work; performance and operations only when load or latency is material. If totals are close, prefer fewer components and known skills.

## Confidence

Do not invent a percentage. Score each evidence factor as `0` (unknown/weak), `1` (partial), or `2` (complete/strong):

- requirements completeness;
- constraint completeness;
- technology-profile quality;
- decision gap between the first and second candidate;
- existing-stack certainty, when applicable.

Calculate the available-points ratio. Report `high` at 0.80 or above, `medium` at 0.55–0.79, and `low` below 0.55. Use `python scripts/confidence.py` when writing an artifact. Always include a prose basis naming the uncertainty that reduced confidence.
