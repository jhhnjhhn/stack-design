# Queue and messaging

Use synchronous work until latency or reliability requires background execution. Start with database-backed jobs for modest workloads and minimal operations. Choose a language-native worker when its ecosystem matters, a managed queue when cloud operations fit, RabbitMQ/NATS for routing or low-latency messaging, and Kafka only for durable high-throughput replayable streams with multiple consumers. Specify retries, idempotency, ordering, poison messages, and observability.
