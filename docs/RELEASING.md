# Releasing Stack Design

Use a pull request for every public release. Do not release directly from an unverified working tree.

## Checklist

1. Confirm `git status --short` contains only intended public files. The private requirements document must remain ignored.
2. Update `CHANGELOG.md` and choose a Semantic Versioning number.
3. Synchronize both plugin manifests:

   ```bash
   python scripts/bump_plugin_version.py <version>
   ```

4. Run the full deterministic validation:

   ```bash
   python scripts/validate_all.py
   python -m compileall -q plugins/stack-design/skills/stack-design/scripts scripts tests
   ```

5. Open a pull request and wait for every CI matrix job to pass.
6. From a clean checkout, install the marketplace and smoke-test a quick recommendation and an existing-repository review.
7. Merge the pull request, create a signed `v<version>` tag when commit signing is configured (otherwise use an annotated tag), and publish GitHub release notes from the changelog.

For `1.0.0`, first confirm that the recommendation schema and public plugin behavior are stable enough to support backward compatibility.

## One-time GitHub setup

- Add a concise repository description and the topics `codex`, `claude-code`, `agent-skill`, `technology-stack`, and `software-architecture`.
- Protect `main`: require a pull request, require the `validate` checks, block force pushes, and block branch deletion.
- Enable Issues, private vulnerability reporting, secret scanning, and push protection where the account plan supports them.
- Keep Actions permissions read-only by default; grant additional permissions only to a workflow that demonstrably needs them.
