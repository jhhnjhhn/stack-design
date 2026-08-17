#!/usr/bin/env python3
"""Render a validated structured recommendation as readable Markdown."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from self_check import check_structured


def render(data: dict) -> str:
    lines = ["# Stack Recommendation", "", "## Context", "", data["context"]["summary"], "", "## Hard Constraints", ""]
    lines += [f"- {item}" for item in data["hard_constraints"]] or ["- None identified."]
    lines += ["", "## Architecture", "", f"**{data['architecture']['choice']}** — {data['architecture']['reason']}", "", "## Recommended Stack", "", "| Layer | Choice | Confidence | Reason |", "|---|---|---|---|"]
    for item in data["selected"]:
        lines.append(f"| {item['layer']} | {item['technology']} | {item['confidence']['level'].title()} | {item['reason']} |")
    sections = (("Alternatives Considered", "alternatives"), ("Rejected Technologies", "rejected"), ("Overengineering Check", "overengineering"))
    for title, key in sections:
        lines += ["", f"## {title}", ""]
        for item in data[key]:
            if isinstance(item, dict):
                name = item.get("technology", item.get("choice", "Item"))
                detail = item.get("reason", item.get("status", ""))
                lines.append(f"- **{name}:** {detail}")
            else:
                lines.append(f"- {item}")
        if not data[key]:
            lines.append("- None.")
    for title, key in (("Risks", "risks"), ("Assumptions", "assumptions")):
        lines += ["", f"## {title}", ""] + ([f"- {item}" for item in data[key]] or ["- None."])
    lines += ["", "## Scaling Triggers", ""]
    for item in data["scaling_triggers"]:
        lines.append(f"- If {item['condition']}, evaluate {item['evaluate']}.")
    if not data["scaling_triggers"]:
        lines.append("- No advanced scaling technology is currently justified.")
    lines += ["", "## Evolution Path", ""]
    for phase in data["evolution_path"]:
        lines.append(f"- **{phase.get('phase', 'phase')}:** {'; '.join(phase.get('changes', []))}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("output", nargs="?")
    args = parser.parse_args()
    source = Path(args.input)
    data = json.loads(source.read_text(encoding="utf-8"))
    profile_dir = Path(__file__).parents[1] / "references" / "technologies"
    _, _, failures = check_structured(data, profile_dir)
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    output = render(data)
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
