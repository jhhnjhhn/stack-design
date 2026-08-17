# AI and ML

Start with a model API and explicit cost, latency, privacy, evaluation, and fallback controls. Use Python when model/data/media libraries require it, but avoid a second service if the existing backend can reliably call the API. For RAG, start with object storage, background ingestion, and PostgreSQL + pgvector when it fits. Add dedicated model serving or a vector database only after measured constraints.
