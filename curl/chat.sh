#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${FLATKEY_AI_KEY:-}" ]]; then
  echo "Missing env var: FLATKEY_AI_KEY" >&2
  echo 'Run: export FLATKEY_AI_KEY="sk-..."' >&2
  exit 1
fi

MODEL="${FLATKEY_CHAT_MODEL:-gpt-5.5}"

curl https://router.flatkey.ai/v1/chat/completions \
  -H "Authorization: Bearer ${FLATKEY_AI_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${MODEL}\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"Hello from Flatkey curl\"}
    ]
  }"
