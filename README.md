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
├── .github/workflows/validate-skill.yml
├── README.md
├── scripts/
│   ├── publish.sh
│   ├── smoke-test.sh
│   └── validate-skill.py
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

Quick repo-native validation:

```bash
python3 scripts/validate-skill.py
bash scripts/smoke-test.sh
```

Optional OpenClaw validator:

```bash
python3 ~/.nvm/versions/node/v22.22.1/lib/node_modules/openclaw/skills/skill-creator/scripts/quick_validate.py ./self-improving-openclaw
```

## Publish from this repo

If you are already logged into ClawHub:

```bash
bash scripts/publish.sh 1.0.1 "Short changelog here"
```

If not logged in yet:

```bash
npx clawhub@latest login
bash scripts/publish.sh 1.0.1 "Short changelog here"
```

## CI

This repo includes a GitHub Actions workflow:

- `.github/workflows/validate-skill.yml`

It automatically:
- validates the skill structure
- runs the init script in a temporary workspace
- verifies the init script is idempotent

## GitHub release

- Repo tag/release target: `v1.0.0`

## Why this exists

This repo is the clean standalone home for the skill, separate from the broader OpenClaw workspace repo where it was first authored.
