# Flatkey Image Buddy

Image generation sample for Flatkey through the OpenAI-compatible router.

## Run

```bash
export FLATKEY_AI_KEY="sk-..."
npm install
npm start -- "a friendly robot holding a Flatkey keycard"
```

Optional:

```bash
export FLATKEY_IMAGE_MODEL="gpt-image-1"
```

The script calls `https://router.flatkey.ai/v1` and writes `output.png` when the API returns base64 image data.
