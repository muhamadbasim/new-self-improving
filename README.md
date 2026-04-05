# new-self-improving

A dedicated repository for the **Self-Improving OpenClaw** skill.

## What this repo contains

- `self-improving-openclaw/` — the published AgentSkill
- structured learning loop for OpenClaw agents:
  - raw intake in `.learnings/`
  - tiered memory in `.self-improving/`
  - promotion rules to `SOUL.md`, `AGENTS.md`, `TOOLS.md`, and `MEMORY.md`
  - heartbeat review workflow
  - workspace initialization script

## Published skill

- ClawHub: <https://clawhub.ai/muhamadbasim/self-improving-openclaw>
- Slug: `self-improving-openclaw`
- Current version: `1.0.0`

## Repo layout

```text
new-self-improving/
├── README.md
└── self-improving-openclaw/
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── assets/
```

## Install from ClawHub

```bash
npx clawhub@latest install self-improving-openclaw
```

For a separate workspace:

```bash
npx clawhub@latest --workdir /path/to/workspace install self-improving-openclaw
```

## Initialize workspace state

After installation, run:

```bash
bash skills/self-improving-openclaw/scripts/init-workspace.sh
```

This creates:

- `.learnings/`
- `.self-improving/`

without overwriting existing files.

## Local validation

Validate the bundled skill locally with the OpenClaw skill-creator validator:

```bash
python3 ~/.nvm/versions/node/v22.22.1/lib/node_modules/openclaw/skills/skill-creator/scripts/quick_validate.py ./self-improving-openclaw
```

## Smoke test

Example install + init test in a temporary workspace:

```bash
mkdir -p /tmp/self-improving-test
npx clawhub@latest --workdir /tmp/self-improving-test install self-improving-openclaw
bash /tmp/self-improving-test/skills/self-improving-openclaw/scripts/init-workspace.sh /tmp/self-improving-test
find /tmp/self-improving-test -maxdepth 2 -type f | sort
```

## Why this exists

This repo is the clean standalone home for the skill, separate from the broader OpenClaw workspace repo where it was first authored.
