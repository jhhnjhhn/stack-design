# Decision principles

1. Start from the real problem and hard constraints, not a fashionable stack.
2. Choose the smallest set of mature components that satisfies current requirements.
3. Prefer existing team skills, company standards, and deployed assets over small theoretical gains.
4. Default to a modular monolith and one primary relational database.
5. PostgreSQL is the default relational candidate unless constraints favor another database.
6. Treat novelty, additional runtimes, network boundaries, and managed vendors as costs.
7. Never recommend a rewrite unless demonstrated long-term benefit clearly exceeds migration and regression cost.
8. Pair every future option with a measurable trigger; do not design for hypothetical scale.
9. Explain why each choice fits and why meaningful alternatives do not.
10. Include AI coding compatibility: documentation, examples, type information, API stability, error clarity, ecosystem maturity, upgrade risk, and tooling.

Decision precedence: hard constraints > organization constraints > existing assets > requirements > team fit > lifecycle cost > performance > popularity.
