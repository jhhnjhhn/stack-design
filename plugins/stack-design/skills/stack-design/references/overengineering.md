# Overengineering checks

- **Microservices:** reject when a small team lacks independent deployment, scaling, ownership, isolation, or materially different service lifecycles. Prefer a modular monolith.
- **Kafka:** require durable high-throughput streams plus replay, multiple consumer groups, event sourcing, or similarly strong evidence.
- **Kubernetes:** require multi-service/multi-node operations, high availability or autoscaling, and a team/platform able to operate it.
- **Redis:** require a measured hot path, shared session, rate limit, distributed lock, queue/broker, or expensive repeated computation. Do not add it as a reflexive cache.
- **Elasticsearch/OpenSearch:** require search quality or scale beyond SQL/PostgreSQL full-text search.
- **GraphQL:** require client/query flexibility that outweighs schema, authorization, caching, and operational complexity.
- **Vector database:** start with pgvector when relational metadata and initial vector scale fit PostgreSQL.
- **Multiple databases:** keep one primary store until distinct workload requirements clearly justify another.
- **Full observability:** start with structured logs, then add metrics, tracing, and a platform when operational evidence demands them.

State `PASS`, `WARN`, or `FAIL` for each relevant item and cite the requirement that justifies an advanced component.
