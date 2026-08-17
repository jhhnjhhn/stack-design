# API style

Default to REST for broad interoperability and simple resources. Use GraphQL for demonstrated multi-client query-shape complexity, gRPC for controlled service-to-service contracts and performance, and tRPC only across a tightly coupled TypeScript boundary. Document versioning, errors, idempotency, pagination, and authorization regardless of style.
