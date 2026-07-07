# Como usar Flatkey

[![GitHub stars](https://img.shields.io/github/stars/flatkey-ai/how-to-use-flatkey?style=social)](https://github.com/flatkey-ai/how-to-use-flatkey/stargazers)

Idiomas: [English](README.md) | [日本語](README.jp.md) | [中文](README.cn.md) | Español | [Português](README.pt.md)

Proyectos de ejemplo para llamar a Flatkey mediante el router compatible con OpenAI.

## Configuracion

```bash
export FLATKEY_AI_KEY="sk-..."
```

Todos los ejemplos usan:

```text
https://router.flatkey.ai/v1
```

Valores opcionales:

```bash
export FLATKEY_CHAT_MODEL="gpt-5.5"
export FLATKEY_IMAGE_MODEL="gpt-image-1"
```

## Ejemplos

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

El ejemplo de imagen escribe `output.png` cuando la API devuelve datos de imagen en base64.

## Verificar sin llamadas API

```bash
python3 -m unittest tests.test_project_layout -v
python3 -m py_compile python/main.py
node --check nodejs/index.mjs
node --check image-buddy/generate-image.mjs
bash -n curl/chat.sh
```

## Monitoreo de stars

Este repositorio incluye un workflow de GitHub Actions que registra el conteo actual de GitHub stars en `stars.json` cada dia y en ejecuciones manuales.
