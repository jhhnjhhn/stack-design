# Realtime application

Define directionality, connection count, latency, ordering, presence, offline behavior, fan-out, and reconnect semantics. Choose polling, SSE, or WebSocket at the simplest sufficient level. Keep durable state in the primary database; introduce Pub/Sub when multiple application instances need fan-out.
