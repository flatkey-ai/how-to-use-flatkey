from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProjectLayoutTest(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "README.jp.md",
            "README.cn.md",
            "README.es.md",
            "README.pt.md",
            "LICENSE",
            ".env.example",
            ".gitignore",
            "stars.json",
            ".github/workflows/star-monitor.yml",
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

    def test_readme_links_languages_and_star_badge(self):
        content = read("README.md")
        for language_readme in [
            "README.jp.md",
            "README.cn.md",
            "README.es.md",
            "README.pt.md",
        ]:
            with self.subTest(language_readme=language_readme):
                self.assertIn(language_readme, content)
        self.assertIn("github/stars/flatkey-ai/how-to-use-flatkey", content)

    def test_localized_readmes_keep_sample_commands(self):
        for language_readme in [
            "README.jp.md",
            "README.cn.md",
            "README.es.md",
            "README.pt.md",
        ]:
            content = read(language_readme)
            with self.subTest(language_readme=language_readme):
                self.assertIn("FLATKEY_AI_KEY", content)
                self.assertIn("https://router.flatkey.ai/v1", content)
                self.assertIn("nodejs", content)
                self.assertIn("python", content)
                self.assertIn("curl", content)
                self.assertIn("image-buddy", content)

    def test_star_monitor_workflow_updates_stars_json(self):
        workflow = read(".github/workflows/star-monitor.yml")
        stars = read("stars.json")
        self.assertIn("schedule:", workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("stargazers_count", workflow)
        self.assertIn("stars.json", workflow)
        self.assertIn('"repository": "flatkey-ai/how-to-use-flatkey"', stars)
        self.assertIn('"history"', stars)

    def test_mit_license_is_present(self):
        license_text = read("LICENSE")
        readme = read("README.md")
        self.assertIn("MIT License", license_text)
        self.assertIn("Flatkey", license_text)
        self.assertIn("[MIT](LICENSE)", readme)


if __name__ == "__main__":
    unittest.main()
