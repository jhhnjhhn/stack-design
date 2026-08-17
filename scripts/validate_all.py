#!/usr/bin/env python3
"""Run every deterministic repository validation and keep reporting after failures."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "plugins" / "stack-design" / "skills" / "stack-design"
COMMANDS = (
    [sys.executable, str(SKILL / "scripts" / "validate_profiles.py")],
    [sys.executable, str(ROOT / "tests" / "run_scenarios.py")],
    [sys.executable, str(ROOT / "tests" / "test_evaluator.py")],
    [sys.executable, str(ROOT / "tests" / "test_tools.py")],
    [sys.executable, str(ROOT / "tests" / "check_references.py")],
    [sys.executable, str(SKILL / "scripts" / "self_check.py"), str(ROOT / "examples" / "internal-image-tool.json")],
    [sys.executable, str(ROOT / "scripts" / "verify_package.py")],
)


def main() -> int:
    failed = 0
    for command in COMMANDS:
        print(f"\n==> {' '.join(command[1:])}", flush=True)
        result = subprocess.run(command, cwd=ROOT, check=False)
        failed += result.returncode != 0
    print(f"\n{'[PASS]' if not failed else '[FAIL]'} validation suite: {len(COMMANDS) - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
