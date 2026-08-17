# Database

Start with one primary store. Prefer PostgreSQL for relational application data, transactions, JSON, full-text search, and initial vectors. Keep MySQL when it is an organizational asset. Use SQLite for local, embedded, or low-concurrency single-node work. Require a distinct access pattern or scale before MongoDB, ClickHouse, graph, KV, or vector infrastructure. Evaluate backups, migration tooling, availability, residency, and exit cost.
