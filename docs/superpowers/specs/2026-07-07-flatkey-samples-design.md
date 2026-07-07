# Flatkey Samples Design

## Goal

Create one sample repository for Flatkey with four runnable examples: Node.js, Python, curl, and image-buddy.

## Structure

- `nodejs/`: OpenAI JavaScript SDK chat completion sample.
- `python/`: OpenAI Python SDK chat completion sample.
- `curl/`: shell script using `curl` against Flatkey router.
- `image-buddy/`: image generation sample project using OpenAI-compatible image API.
- Root docs/config: `README.md`, `.env.example`, `.gitignore`.

## Runtime Contract

All samples read `FLATKEY_AI_KEY` and use `https://router.flatkey.ai/v1`.
Chat samples default to `gpt-5.5`.
Image samples default to `gpt-image-1`.

## Error Handling

Samples fail fast when `FLATKEY_AI_KEY` is missing and print the exact export command shape.

## Verification

Verification does not call the live API. It checks project layout, required strings, and script syntax.
