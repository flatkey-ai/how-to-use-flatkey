from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProjectLayoutTest(unittest.TestCase):
    def test_required_files_exist(self):
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
        self.assertEqual(missing, [])

    def test_samples_use_flatkey_router_and_env_var(self):
        paths = [
            "nodejs/index.mjs",
            "python/main.py",
            "curl/chat.sh",
            "image-buddy/generate-image.mjs",
        ]
        for path in paths:
            with self.subTest(path=path):
                content = read(path)
                self.assertIn("https://router.flatkey.ai/v1", content)
                self.assertIn("FLATKEY_AI_KEY", content)

    def test_readme_documents_all_samples(self):
        content = read("README.md")
        for name in ["nodejs", "python", "curl", "image-buddy"]:
            with self.subTest(name=name):
                self.assertIn(name, content)


if __name__ == "__main__":
    unittest.main()
