# Migration decisions

Establish the current pain with evidence. Compare `KEEP`, `PARTIAL`, and `MIGRATE` against migration cost, data movement, dual writes, regressions, team learning, operational change, and rollback. A new technology must solve the stated bottleneck; preference or popularity is insufficient.

Prefer strangler-style replacement and reversible boundaries. Define success metrics, compatibility period, rollback, data validation, and an exit strategy. Conclude with one decision and confidence. Default to `KEEP` when the current framework is not the bottleneck.
