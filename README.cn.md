# 如何使用 Flatkey

[![GitHub stars](https://img.shields.io/github/stars/flatkey-ai/how-to-use-flatkey?style=social)](https://github.com/flatkey-ai/how-to-use-flatkey/stargazers)

语言: [English](README.md) | [日本語](README.jp.md) | 中文 | [Español](README.es.md) | [Português](README.pt.md)

这些示例项目演示如何通过 OpenAI 兼容路由调用 Flatkey。

## 设置

```bash
export FLATKEY_AI_KEY="sk-..."
```

所有示例都使用：

```text
https://router.flatkey.ai/v1
```

可选覆盖：

```bash
export FLATKEY_CHAT_MODEL="gpt-5.5"
export FLATKEY_IMAGE_MODEL="gpt-image-1"
```

## 示例

### nodejs

```bash
cd nodejs
npm install
npm start
```

### python

```bash
cd python
python3 -m pip install -r requirements.txt
python3 main.py
```

### curl

```bash
cd curl
chmod +x chat.sh
./chat.sh
```

### image-buddy

```bash
cd image-buddy
npm install
npm start -- "a friendly robot holding a Flatkey keycard"
```

如果图片 API 返回 base64 图片数据，`image-buddy` 会写入 `output.png`。

## 不调用 API 的验证

```bash
python3 -m unittest tests.test_project_layout -v
python3 -m py_compile python/main.py
node --check nodejs/index.mjs
node --check image-buddy/generate-image.mjs
bash -n curl/chat.sh
```

## Star 监控

本仓库包含 GitHub Actions workflow。它会每天或手动运行时读取当前 GitHub star 数，并写入 `stars.json`。
