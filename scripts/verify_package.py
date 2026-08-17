#!/usr/bin/env python3
"""Verify plugin manifests, marketplace wiring, skill metadata, and README catalog counts."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).parents[1]
PLUGIN = ROOT / "plugins" / "stack-design"
SKILL = PLUGIN / "skills" / "stack-design"
EXPECTED_AUTHOR = "naoyouge"
PRIVATE_REQUIREMENTS = "/docs/stack-design-requirements.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    failures = []
    codex = load(PLUGIN / ".codex-plugin" / "plugin.json")
    claude = load(PLUGIN / ".claude-plugin" / "plugin.json")
    marketplace = load(ROOT / ".agents" / "plugins" / "marketplace.json")
    claude_marketplace = load(ROOT / ".claude-plugin" / "marketplace.json")
    if codex.get("name") != "stack-design" or claude.get("name") != "stack-design":
        failures.append("plugin names must be stack-design")
    if codex.get("version") != claude.get("version") or not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", codex.get("version", "")):
        failures.append("Codex and Claude manifests need matching semver versions")
    if codex.get("author", {}).get("name") != EXPECTED_AUTHOR or claude.get("author", {}).get("name") != EXPECTED_AUTHOR:
        failures.append(f"plugin author must be {EXPECTED_AUTHOR}")
    if codex.get("interface", {}).get("developerName") != EXPECTED_AUTHOR:
        failures.append(f"Codex developerName must be {EXPECTED_AUTHOR}")
    if claude_marketplace.get("owner", {}).get("name") != EXPECTED_AUTHOR:
        failures.append(f"Claude marketplace owner must be {EXPECTED_AUTHOR}")
    if codex.get("skills") != "./skills/" or not (PLUGIN / "skills" / "stack-design" / "SKILL.md").is_file():
        failures.append("Codex skills path is invalid")
    entry = next((item for item in marketplace.get("plugins", []) if item.get("name") == "stack-design"), None)
    if not entry or entry.get("source", {}).get("path") != "./plugins/stack-design":
        failures.append("Codex marketplace entry is missing or miswired")
    centry = next((item for item in claude_marketplace.get("plugins", []) if item.get("name") == "stack-design"), None)
    if not centry or centry.get("source") != "./plugins/stack-design":
        failures.append("Claude marketplace entry is missing or miswired")
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", skill_text, re.DOTALL)
    if not match:
        failures.append("SKILL.md frontmatter is invalid")
    else:
        keys = {line.split(":", 1)[0].strip() for line in match.group(1).splitlines() if ":" in line}
        if keys != {"name", "description"}:
            failures.append(f"SKILL.md frontmatter keys must be name and description, got {sorted(keys)}")
    openai_yaml = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$stack-design" not in openai_yaml:
        failures.append("agents/openai.yaml default prompt must mention $stack-design")
    text_suffixes = {".md", ".json", ".yaml", ".yml", ".py", ".txt"}
    all_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts and path.suffix.lower() in text_suffixes
    )
    if ("[" + "TODO:") in all_text:
        failures.append("package contains TODO placeholders")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    version = codex.get("version", "")
    if f"version-{version}-blue" not in readme:
        failures.append(f"README version badge is stale: expected {version}")
    if not re.search(rf"^## {re.escape(version)}(?:\s+-|$)", changelog, re.MULTILINE):
        failures.append(f"CHANGELOG has no release heading for {version}")
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    if PRIVATE_REQUIREMENTS not in {line.strip() for line in gitignore}:
        failures.append(f"private requirements document must be ignored as {PRIVATE_REQUIREMENTS}")
    try:
        tracked_private_doc = subprocess.run(
            ["git", "ls-files", "--error-unmatch", PRIVATE_REQUIREMENTS.lstrip("/")],
            cwd=ROOT,
            capture_output=True,
            check=False,
        )
    except OSError:
        tracked_private_doc = None
    if tracked_private_doc is not None and tracked_private_doc.returncode == 0:
        failures.append("private requirements document must not be stored inside .git")
    counts = {
        "decision categories": len(list((SKILL / "references" / "categories").glob("*.md"))),
        "project types": len(list((SKILL / "references" / "project-types").glob("*.md"))),
        "technology profiles": len(list((SKILL / "references" / "technologies").glob("*.md"))),
        "scenario definitions": len(load(ROOT / "tests" / "scenarios" / "scenarios.json")),
    }
    for label, count in counts.items():
        if f"{count} {label}" not in readme:
            failures.append(f"README catalog count is stale: expected '{count} {label}'")
    for failure in failures:
        print(f"[FAIL] {failure}")
    if failures:
        return 1
    print(f"[PASS] plugin package {version} is wired correctly and release metadata is synchronized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
