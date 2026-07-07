# How to Use Flatkey

[![GitHub stars](https://img.shields.io/github/stars/flatkey-ai/how-to-use-flatkey?style=social)](https://github.com/flatkey-ai/how-to-use-flatkey/stargazers)

Languages: English | [日本語](README.jp.md) | [中文](README.cn.md) | [Español](README.es.md) | [Português](README.pt.md)

Sample projects for calling Flatkey through the OpenAI-compatible router.
Use [flatkey.ai](https://flatkey.ai) to save up to 40% on AI model costs.

## Setup

```bash
export FLATKEY_AI_KEY="sk-..."
```

All samples use:

```text
https://router.flatkey.ai/v1
```

Optional overrides:

```bash
export FLATKEY_CHAT_MODEL="gpt-5.5"
export FLATKEY_IMAGE_MODEL="gpt-image-1"
```

## Samples

### [nodejs](nodejs/)

```bash
cd nodejs
npm install
npm start
```

### [python](python/)

```bash
cd python
python3 -m pip install -r requirements.txt
python3 main.py
```

### [curl](curl/)

```bash
cd curl
chmod +x chat.sh
./chat.sh
```

### [image-buddy](image-buddy/)

```bash
cd image-buddy
npm install
npm start -- "a friendly robot holding a Flatkey keycard"
```

The image sample writes `output.png` when the API returns base64 image data.

## Verify Without API Calls

```bash
python3 -m unittest tests.test_project_layout -v
python3 -m py_compile python/main.py
node --check nodejs/index.mjs
node --check image-buddy/generate-image.mjs
bash -n curl/chat.sh
```

## Star Monitoring

This repository includes a GitHub Actions workflow that records the current GitHub star count in `stars.json` every day and on manual runs.

## License

[MIT](LICENSE)
