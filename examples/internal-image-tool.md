# Stack Recommendation

## Context

Greenfield internal image asset tool for five users; React is preferred, Python is required for OpenCV and AI image workflows, SEO is not required, and deployment is one Linux server.

## Hard Constraints

- Python image-processing ecosystem
- Single Linux server
- No SEO or SSR requirement

## Architecture

**modular-monolith** — One small team owns one product and no capability requires an independent deployment lifecycle.

## Recommended Stack

| Layer | Choice | Confidence | Reason |
|---|---|---|---|
| frontend | React | High | It preserves the team's existing preference for an interactive private UI. |
| frontend build | Vite | High | A client SPA does not need an SSR server or framework caching model. |
| backend | FastAPI | High | It keeps the API in the Python runtime already required by media processing. |
| database | PostgreSQL | High | Relational asset, project, user, and job metadata fit one transactional source of truth. |
| object storage | MinIO | Medium | Private deployment benefits from an S3-compatible binary-storage boundary. |
| background jobs | Dramatiq with Redis broker | Medium | Image generation and transformation must execute outside request latency; Redis is justified only as the broker. |
| queue broker | Redis | Medium | It is broker infrastructure for the selected worker, not a speculative application cache. |
| deployment | Docker Compose | High | It operates the web, API, worker, database, broker, and storage processes on one server without a cluster control plane. |

## Alternatives Considered

- **Database-backed jobs:** Prefer this if initial retries and throughput remain modest.
- **Managed S3:** Prefer this if public cloud is allowed and reduced operations outweigh provider dependence.

## Rejected Technologies

- **Next.js:** No SEO or SSR requirement.
- **Kafka:** No replayable stream or multiple consumer-group requirement.
- **Kubernetes:** Single-server deployment has no orchestration requirement.
- **Elasticsearch:** No search requirement beyond PostgreSQL.
- **Microservices:** One team and one deployment lifecycle favor a modular monolith.

## Overengineering Check

- **Redis:** Used as a queue broker, not an application cache.
- **Kafka:** Streaming triggers are absent.
- **Kubernetes:** Multi-node HA and platform operations are absent.

## Risks

- Self-hosted MinIO and Redis require backup and monitoring.
- Job volume is not yet measured.

## Assumptions

- Initial job volume is modest.
- Brief maintenance windows are acceptable.

## Scaling Triggers

- If queue latency breaches the product target after worker tuning, evaluate a managed queue or horizontally scaled workers.
- If multi-node high availability becomes a current requirement, evaluate an orchestration platform.

## Evolution Path

- **MVP:** Use the selected modular monolith and one server.
- **Measured growth:** Change the queue or deployment only when its trigger is observed.
