# Flatkey Samples Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Flatkey sample repository with Node.js, Python, curl, and image generation examples.

**Architecture:** Keep each sample self-contained in its own directory. Share only environment variable names and Flatkey router URL through docs and `.env.example`.

**Tech Stack:** Node.js ESM, Python OpenAI SDK, bash/curl, OpenAI-compatible image API.

---

### Task 1: Add Layout Smoke Tests

**Files:**
- Create: `tests/test_project_layout.py`

- [ ] **Step 1: Add tests that describe the required sample repository layout**

```python
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_required_files_exist():
    required = [
        "README.md",
        ".env.example",
        ".gitignore",
        "nodejs/package.json",
        "nodejs/index.mjs",
        "python/requirements.txt",
        "python/main.py",
        "curl/chat.sh",
        "image-buddy/package.json",
        "image-buddy/generate-image.mjs",
        "image-buddy/README.md",
    ]
    missing = [path for path in required if not (ROOT / path).exists()]
    assert missing == []


def test_samples_use_flatkey_router_and_env_var():
    paths = [
        "nodejs/index.mjs",
        "python/main.py",
        "curl/chat.sh",
        "image-buddy/generate-image.mjs",
    ]
    for path in paths:
        content = read(path)
        assert "https://router.flatkey.ai/v1" in content
        assert "FLATKEY_AI_KEY" in content


def test_readme_documents_all_samples():
    content = read("README.md")
    for name in ["nodejs", "python", "curl", "image-buddy"]:
        assert name in content
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python3 -m unittest tests.test_project_layout -v`
Expected: failure because sample files do not exist yet.

### Task 2: Create Sample Files

**Files:**
- Create: `README.md`
- Create: `.env.example`
- Create: `.gitignore`
- Create: `nodejs/package.json`
- Create: `nodejs/index.mjs`
- Create: `python/requirements.txt`
- Create: `python/main.py`
- Create: `curl/chat.sh`
- Create: `image-buddy/package.json`
- Create: `image-buddy/generate-image.mjs`
- Create: `image-buddy/README.md`
- Delete: `requirements.txt`
- Delete: `test_flatkey.py`

- [ ] **Step 1: Add sample files exactly matching the approved structure**
- [ ] **Step 2: Run syntax checks**

Run: `python3 -m py_compile python/main.py && node --check nodejs/index.mjs && node --check image-buddy/generate-image.mjs && bash -n curl/chat.sh`
Expected: no output, exit code 0.

- [ ] **Step 3: Run layout tests**

Run: `python3 -m unittest tests.test_project_layout -v`
Expected: all tests pass.

### Task 3: Initialize Git And Push

**Files:**
- Modify: git metadata only.

- [ ] **Step 1: Initialize git when no repository exists**

Run: `git init`
Expected: repository initialized.

- [ ] **Step 2: Commit sample project**

Run: `git add . && git commit -m "feat: add Flatkey sample projects"`
Expected: commit created.

- [ ] **Step 3: Add remote and push main**

Run: `git remote add origin git@github.com:flatkey-ai/how-to-use-flatkey.git && git branch -M main && git push -u origin main`
Expected: `main` pushed to GitHub.
