import OpenAI from "openai";

const apiKey = process.env.FLATKEY_AI_KEY;

if (!apiKey) {
  console.error("Missing env var: FLATKEY_AI_KEY");
  console.error('Run: export FLATKEY_AI_KEY="sk-..."');
  process.exit(1);
}

const client = new OpenAI({
  apiKey,
  baseURL: "https://router.flatkey.ai/v1",
});

const model = process.env.FLATKEY_CHAT_MODEL || "gpt-5.5";
const prompt = process.argv.slice(2).join(" ") || "Hello from Flatkey Node.js";

const response = await client.chat.completions.create({
  model,
  messages: [{ role: "user", content: prompt }],
});

console.log(response.choices[0].message.content);
