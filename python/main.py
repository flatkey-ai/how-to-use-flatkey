import os
import sys

try:
    from openai import OpenAI
except ModuleNotFoundError:
    print("Missing dependency: openai")
    print("Install with: python3 -m pip install -r requirements.txt")
    sys.exit(1)


api_key = os.environ.get("FLATKEY_AI_KEY")
if not api_key:
    print("Missing env var: FLATKEY_AI_KEY")
    print('Run: export FLATKEY_AI_KEY="sk-..."')
    sys.exit(1)


client = OpenAI(
    api_key=api_key,
    base_url="https://router.flatkey.ai/v1",
)

model = os.environ.get("FLATKEY_CHAT_MODEL", "gpt-5.5")
prompt = " ".join(sys.argv[1:]) or "Hello from Flatkey Python"

response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
