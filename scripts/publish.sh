#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="${1:-}"
CHANGELOG="${2:-}"

if [[ -z "$VERSION" ]]; then
  echo "Usage: scripts/publish.sh <version> [changelog]" >&2
  exit 1
fi

if [[ -z "$CHANGELOG" ]]; then
  CHANGELOG="Release $VERSION"
fi

cd "$ROOT"
exec npx clawhub@latest publish \
  --slug new-self-improving \
  --name "new-self-improving" \
  --version "$VERSION" \
  --tags latest \
  --changelog "$CHANGELOG" \
  ./new-self-improving
