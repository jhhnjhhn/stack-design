# Stack Design

[![CI](https://github.com/jhhnjhhn/stack-design/actions/workflows/ci.yml/badge.svg)](https://github.com/jhhnjhhn/stack-design/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](CHANGELOG.md)

**Technology judgment for AI coding agents.**

Your coding agent already knows hundreds of frameworks. The hard part is knowing when **not** to use them.

One plugin for Codex and Claude Code, with a shared Agent Skill for other compatible tools. It reads the real requirements, constraints, team context, deployment environment, and existing codebase before recommending a stack—and explains every trade-off.

No default Kafka. No speculative Kubernetes. No rewrite because a newer framework looks nicer.

---

## Why I built it

Ask an AI agent to build a five-user internal tool and it may confidently reach for Next.js, NestJS, Redis, Kafka, Elasticsearch, Kubernetes, Prometheus, and Grafana.

The code might work. The decision is still wrong.

AI coding agents have broad technology knowledge, but technology selection is not a recall problem. It is a judgment problem: which constraints matter, which complexity is justified now, which existing assets should be preserved, and what evidence should trigger the next architectural step.

So this project turns the quiet judgment of a senior engineer, Tech Lead, or architect into a reusable agent skill.

> **Choose the simplest stack that satisfies the real constraints.**

---

## What it decides

| Area | Decisions |
|---|---|
| Architecture | Monolith · modular monolith · microservices · event-driven · serverless · edge |
| Frontend | SPA · SSR · SSG · React · Vue · Svelte · Angular · Vite · Next.js · Nuxt · Astro |
| Backend | Python · TypeScript · Java · C# · Go · framework fit |
| Data | PostgreSQL · MySQL · SQLite · MongoDB · analytics · vector search |
| Infrastructure | Cache · queues · object storage · search · deployment · CI/CD · observability |
| Product boundaries | Auth · realtime · API style · AI/ML workloads |
| Change strategy | Keep · add · replace · remove · migrate · write an ADR |

Every full recommendation includes:

- selected technologies and confidence;
- alternatives and explicitly rejected options;
- trade-offs, risks, and assumptions;
- an overengineering check;
- measurable scaling triggers;
- an evolution and exit path.

---

## Before / after

**The requirement**

```text
5-person internal image asset tool
React preferred
Python image processing and AI image generation
No SEO
One Linux server
```

**A stack assembled from popular defaults**

```text
Next.js + NestJS + PostgreSQL + Redis
Kafka + Elasticsearch + Kubernetes
```

**Stack Design**

| Layer | Choice | Why |
|---|---|---|
| Architecture | Modular monolith | One team, one product, no independent service lifecycle |
| Frontend | React + Vite | Existing preference; private SPA; no SSR or SEO |
| Backend | FastAPI | Python is already required by the media workflow |
| Database | PostgreSQL | One relational source of truth |
| Storage | S3-compatible storage | Keep binaries outside the database |
| Jobs | Database jobs first; broker-backed worker when justified | Async processing is real; streaming is not |
| Deployment | Docker Compose | A few processes on one Linux server |

**Rejected**

```text
Next.js       → no SSR or SEO requirement
Kafka         → no replayable event stream or consumer groups
Kubernetes    → no multi-node HA or orchestration requirement
Elasticsearch → PostgreSQL search is sufficient initially
```

The point is not that these technologies are bad. The point is that every technology must earn its place.

---

## Install

**Codex**

```bash
codex plugin marketplace add jhhnjhhn/stack-design
codex plugin add stack-design@stack-design
```

**Claude Code**

```text
/plugin marketplace add jhhnjhhn/stack-design
/plugin install stack-design@stack-design
```

Restart or reload the agent after installation. The shared entry point is [`plugins/stack-design/skills/stack-design/SKILL.md`](plugins/stack-design/skills/stack-design/SKILL.md); no service, build step, or model API key is required.

### Editable install

Clone the repository anywhere, then link it into your agent's skill directory:

```bash
git clone https://github.com/jhhnjhhn/stack-design.git ~/code/stack-design
ln -s ~/code/stack-design/plugins/stack-design/skills/stack-design ~/.codex/skills/stack-design
```

On Windows, use a directory junction to link `plugins\stack-design\skills\stack-design` into `%USERPROFILE%\.codex\skills\stack-design`.

---

## Quickstart

Ask in natural language:

```text
Use stack-design to choose the stack for a five-person internal image tool.
React is preferred, image processing must use Python, there is no SEO,
and the application runs on one Linux server.
```

Or select a focused mode:

```text
/stack-design
/stack-design quick
/stack-design compare FastAPI NestJS Go
/stack-design existing
/stack-design migrate Flask to FastAPI
/stack-design adr
```

### Existing repository

Point the agent at a codebase and describe the change:

```text
Use stack-design existing. This React + Spring Boot application needs AI summaries.
Should we add a Python service or keep the current backend?
```

The skill scans common manifests, reports the detected stack, and labels decisions as `KEEP`, `ADD`, `REPLACE`, or `REMOVE`. Existing technology creates a strong default bias; a rewrite needs evidence.

### Compare candidates

```text
/stack-design compare FastAPI NestJS Go

Context: three backend engineers know TypeScript, the product is a B2B API,
there are no Python-only dependencies, and the first release is due in six weeks.
```

The result is contextual—not a global framework ranking. Saved decisions use a schema-versioned JSON contract, then render to Markdown; confidence is derived as `low`, `medium`, or `high` from explicit evidence factors rather than invented percentages.

---

## How it works

Stack Design follows a constraint-first decision sequence:

```text
Requirements
  ↓
Hard constraints
  ↓
Existing assets and organization standards
  ↓
Project-type and category rules
  ↓
Candidate technology profiles
  ↓
Structured comparison
  ↓
Overengineering check
  ↓
Recommendation + rejected options + evolution triggers
```

Hard constraints cannot be outvoted by a score. When two candidates both satisfy the requirements, the skill prefers fewer components, known team skills, mature ecosystems, lower operational surface, and better AI-maintainability.

### What loads when

The knowledge base uses progressive disclosure. The agent does not load every technology profile for every decision.

| You ask for… | Agent loads |
|---|---|
| A small internal tool | `SKILL.md` + principles + internal-tool profile + affected categories |
| A Python AI application | The above + AI-app/AI-ML rules + real Python candidates |
| FastAPI vs NestJS | Scoring rules + backend rules + only those candidate profiles |
| Review this repository | Stack detector + detected manifests + affected categories |
| Should we migrate? | Existing-stack evidence + migration rules + source/target profiles |
| Write an ADR | The completed decision + ADR template |

Adding another profile does not increase routine context use. A technology file is loaded only when it becomes a credible candidate.

---

## Architecture

```text
stack-design/
├── .agents/plugins/marketplace.json       — Codex marketplace catalog
├── .claude-plugin/marketplace.json        — Claude marketplace catalog
├── plugins/stack-design/
│   ├── .codex-plugin/plugin.json          — Codex plugin manifest
│   ├── .claude-plugin/plugin.json         — Claude plugin manifest
│   └── skills/stack-design/
│       ├── SKILL.md                       — workflow, routing, output contract
│       ├── agents/openai.yaml             — Codex-facing skill metadata
│       ├── references/
│       │   ├── categories/                — 14 decision domains
│       │   ├── project-types/             — 8 application profiles
│       │   ├── domains/                   — specialist constraints
│       │   └── technologies/              — 68 sourced candidate profiles
│       ├── templates/                     — JSON schema + report templates
│       └── scripts/                       — detection, confidence, validation, rendering
├── examples/                              — structured and rendered decisions
├── scripts/                               — package and release validation
├── tests/                                 — scenarios, evaluator, references, smoke tests
└── docs/adr/                              — settled design decisions
```

The split is deliberate: [`SKILL.md`](plugins/stack-design/skills/stack-design/SKILL.md) stays small enough to guide the agent, while detailed knowledge lives in references that are loaded only when relevant.

---

## Validation

The runtime and repository checks use the Python standard library. Python 3.10+ is sufficient.

```bash
python scripts/validate_all.py
```

To evaluate outputs produced by a real agent, implement the documented runner contract and run:

```bash
python tests/evaluate_scenarios.py --runner path/to/agent-runner --responses .eval-results
```

Current catalog baseline:

```text
14 decision categories
8 project types
68 technology profiles
44 scenario definitions
```

---

## It's working if…

- A small internal tool does not acquire Kafka or Kubernetes without a real requirement.
- An existing application is preserved when its framework is not the bottleneck.
- Every important choice says why it fits this context.
- Every serious alternative says why it lost.
- Missing non-critical information becomes an explicit assumption, not an interrogation.
- Future infrastructure is tied to a measurable trigger, not “we may have one million users someday.”
- `python plugins/stack-design/skills/stack-design/scripts/self_check.py <report.json>` finishes without failures.

If any of these fail, that is a bug worth filing.

---

## When not to use this skill

- **Detailed system design** — use Stack Design to choose technologies, then design components, APIs, and data flows separately.
- **Implementation generation** — this skill chooses the stack; it does not build the whole application.
- **Framework tutorials** — technology profiles contain decision boundaries, not setup guides.
- **Benchmark rankings** — a faster benchmark does not make a technology the best organizational choice.
- **Safety-critical sign-off** — regulated and safety-critical decisions still require qualified human review.

Before adding a technology, ask: *which current requirement would fail without it?* If there is no clear answer, leave it out.

---

## Contributing

Contributions are welcome: technology profiles, project profiles, domain rules, scenarios, decision rules, and bug fixes.

A contribution must explain:

```text
What decision problem does this improve?
Which scenarios does it affect?
What trade-off does it introduce?
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md). New technology profiles need strengths, weaknesses, selection and avoidance conditions, maturity, AI-coding metadata, and at least two affected scenarios.

Maintainers should follow the tested release process in [`docs/RELEASING.md`](docs/RELEASING.md). Security issues belong in a private advisory as described in [`SECURITY.md`](SECURITY.md), never in a public issue.

---

## Inspiration

The product idea and progressive-disclosure approach were inspired by [Cathryn Lavery's Diagram Design](https://github.com/cathrynlavery/diagram-design): one opinionated agent skill, focused references, deterministic checks, and a clear standard for knowing when the output is good enough.

Stack Design applies that philosophy to a different question:

> **Which technologies should this project use—and which ones should it deliberately avoid?**

---

## License

[MIT](LICENSE)

**Pick the right stack before AI writes the wrong code.**
