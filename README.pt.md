# Como usar Flatkey

[![GitHub stars](https://img.shields.io/github/stars/flatkey-ai/how-to-use-flatkey?style=social)](https://github.com/flatkey-ai/how-to-use-flatkey/stargazers)

Idiomas: [English](README.md) | [日本語](README.jp.md) | [中文](README.cn.md) | [Español](README.es.md) | Português

Projetos de exemplo para chamar a Flatkey pelo roteador compativel com OpenAI.

## Configuracao

```bash
export FLATKEY_AI_KEY="sk-..."
```

Todos os exemplos usam:

```text
https://router.flatkey.ai/v1
```

Substituicoes opcionais:

```bash
export FLATKEY_CHAT_MODEL="gpt-5.5"
export FLATKEY_IMAGE_MODEL="gpt-image-1"
```

## Exemplos

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

O exemplo de imagem grava `output.png` quando a API retorna dados de imagem em base64.

## Verificar sem chamadas API

```bash
python3 -m unittest tests.test_project_layout -v
python3 -m py_compile python/main.py
node --check nodejs/index.mjs
node --check image-buddy/generate-image.mjs
bash -n curl/chat.sh
```

## Monitoramento de stars

Este repositorio inclui um workflow do GitHub Actions que registra a contagem atual de GitHub stars em `stars.json` todos os dias e em execucoes manuais.
