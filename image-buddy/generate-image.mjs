import { writeFile } from "node:fs/promises";
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

const model = process.env.FLATKEY_IMAGE_MODEL || "gpt-image-1";
const prompt =
  process.argv.slice(2).join(" ") ||
  "A clean product-style image of a brass key labeled Flatkey on a white desk";

const response = await client.images.generate({
  model,
  prompt,
  size: "1024x1024",
});

const image = response.data?.[0];

if (image?.b64_json) {
  await writeFile("output.png", Buffer.from(image.b64_json, "base64"));
  console.log("Wrote output.png");
} else if (image?.url) {
  console.log(image.url);
} else {
  console.log(JSON.stringify(response, null, 2));
}
