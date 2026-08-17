# Agent evaluation protocol

Scenario definitions are not snapshots of one preferred prose answer. Each case contains a concrete user prompt, technologies that must be selected, technologies that must be explicitly rejected, acceptable optional candidates, and required decision sections.

## Runner contract

An external agent runner receives three positional arguments:

```text
runner <prompt.txt> <response.json> <skill-directory>
```

It must invoke the agent with the supplied Skill and write one JSON response conforming to `templates/recommendation.schema.json`. The evaluator never shells through an interpolated command and remains model-vendor neutral.

Run:

```bash
python tests/evaluate_scenarios.py --runner path/to/runner --responses .eval-results
```

For already collected responses, omit `--runner`:

```bash
python tests/evaluate_scenarios.py --responses .eval-results
```

## Pass conditions

- Every `must_recommend` profile is selected.
- No `must_not_recommend` profile is selected.
- Every forbidden technology is explicitly rejected with a reason.
- Required decision sections, alternatives, and an evolution path are present.
- The structured recommendation independently passes `scripts/self_check.py`.

`tests/test_evaluator.py` constructs valid responses and then injects a forbidden recommendation to prove the evaluator fails in the expected direction. CI runs this deterministic meta-test; live model runs remain an explicit release or research step because they require an installed agent and credentials.
