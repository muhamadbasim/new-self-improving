#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf "$TEST_ROOT"' EXIT

echo "Smoke test workspace: $TEST_ROOT"

bash "$ROOT/new-self-improving/scripts/init-workspace.sh" "$TEST_ROOT"
bash "$ROOT/new-self-improving/scripts/init-workspace.sh" "$TEST_ROOT"

required=(
  "$TEST_ROOT/.learnings/LEARNINGS.md"
  "$TEST_ROOT/.learnings/ERRORS.md"
  "$TEST_ROOT/.learnings/FEATURE_REQUESTS.md"
  "$TEST_ROOT/.learnings/REVIEW_QUEUE.md"
  "$TEST_ROOT/.self-improving/HOT.md"
  "$TEST_ROOT/.self-improving/INDEX.md"
  "$TEST_ROOT/.self-improving/heartbeat-state.md"
)

for file in "${required[@]}"; do
  [[ -f "$file" ]] || { echo "Missing expected file: $file" >&2; exit 1; }
done

echo "OK: smoke test passed"
