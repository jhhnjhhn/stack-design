# Cache

Do not add a cache before measuring a bottleneck. Prefer browser/CDN caching for static responses and process-local caching for disposable single-instance data. Use Redis for shared session, rate limits, locks, queues, or measured hot keys across instances. Define consistency, invalidation, TTL, memory bounds, failure behavior, and a removal test.
