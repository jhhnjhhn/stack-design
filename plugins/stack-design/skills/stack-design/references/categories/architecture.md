# Architecture

Default to a modular monolith. Choose a simple monolith for a tiny, short-lived codebase; preserve clear module boundaries for production. Consider microservices only with independently owned/deployed/scaled capabilities and operational maturity. Use event-driven boundaries for real asynchronous decoupling or streams, serverless for bursty stateless workloads with acceptable platform constraints, edge for demonstrated geographic latency, and hybrid only when incompatible constraints require it.
