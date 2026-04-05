#!/usr/bin/env python3
"""Minimal validator for the bundled AgentSkill.

Checks:
- skill directory exists
- SKILL.md exists
- frontmatter exists
- name matches folder name
- description field exists
- required bundled files exist
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "new-self-improving"
SKILL_MD = SKILL_DIR / "SKILL.md"

REQUIRED_FILES = [
    "scripts/init-workspace.sh",
    "references/logging-format.md",
    "references/promotion-rules.md",
    "references/heartbeat-review.md",
    "references/workspace-layout.md",
    "assets/LEARNINGS.md",
    "assets/ERRORS.md",
    "assets/FEATURE_REQUESTS.md",
    "assets/REVIEW_QUEUE.md",
    "assets/HOT.md",
    "assets/INDEX.md",
    "assets/heartbeat-state.md",
]


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


if not SKILL_DIR.is_dir():
    fail(f"Skill directory missing: {SKILL_DIR}")

if not SKILL_MD.is_file():
    fail("SKILL.md missing")

text = SKILL_MD.read_text(encoding="utf-8")
match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
if not match:
    fail("SKILL.md missing YAML frontmatter")

frontmatter = match.group(1)
name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.MULTILINE)
if not name_match:
    fail("Frontmatter missing valid name field")

name = name_match.group(1).strip()
if name != SKILL_DIR.name:
    fail(f"Frontmatter name '{name}' does not match folder '{SKILL_DIR.name}'")

if not re.search(r"^description:\s*", frontmatter, re.MULTILINE):
    fail("Frontmatter missing description field")

for rel in REQUIRED_FILES:
    path = SKILL_DIR / rel
    if not path.is_file():
        fail(f"Missing required file: {rel}")

print("OK: skill structure looks valid")
