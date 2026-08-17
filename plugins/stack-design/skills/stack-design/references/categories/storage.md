# Object storage

Use local disk only for disposable or explicitly single-node data with backups. Prefer S3-compatible object storage for durable uploads and media. Select managed S3/OSS/COS/GCS/R2 by region, egress, CDN, compliance, and existing cloud; select MinIO for justified private/on-prem S3 compatibility. Keep metadata in the primary database and binary objects outside it.
