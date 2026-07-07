# Flatkey の使い方

[![GitHub stars](https://img.shields.io/github/stars/flatkey-ai/how-to-use-flatkey?style=social)](https://github.com/flatkey-ai/how-to-use-flatkey/stargazers)

言語: [English](README.md) | 日本語 | [中文](README.cn.md) | [Español](README.es.md) | [Português](README.pt.md)

OpenAI 互換ルーター経由で Flatkey を呼び出すサンプルプロジェクトです。

## セットアップ

```bash
export FLATKEY_AI_KEY="sk-..."
```

すべてのサンプルは次の URL を使います。

```text
https://router.flatkey.ai/v1
```

任意の上書き設定:

```bash
export FLATKEY_CHAT_MODEL="gpt-5.5"
export FLATKEY_IMAGE_MODEL="gpt-image-1"
```

## サンプル

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

画像 API が base64 データを返す場合、`image-buddy` は `output.png` を保存します。

## API 呼び出しなしの検証

```bash
python3 -m unittest tests.test_project_layout -v
python3 -m py_compile python/main.py
node --check nodejs/index.mjs
node --check image-buddy/generate-image.mjs
bash -n curl/chat.sh
```

## Star モニタリング

このリポジトリには GitHub Actions ワークフローが含まれます。毎日または手動実行で現在の GitHub star 数を `stars.json` に記録します。
