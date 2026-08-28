import sys
import statistics
from openai import OpenAI
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

prompt = {
    "中文": "用一句话描述一只猫在做什么。",
    "English": "Describe what a cat is doing in one sentence.",
    "日本語": "猫が何をしているかを一文で説明してください。",
}

N = 10
for label, prompt in prompt.items():
    output_tokens = []
    for _ in range(N):
        r = client.chat.completions.create(
            model="qwen3.8:27b",
            max_tokens=100,
            temperature=1.0,
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        output_tokens.append(r.usage.completion_tokens)
    print(f"\n[{label}] prompt: {prompt}")
    print(f"input_tokens: {r.usage.prompt_tokens}")
    print(f"output_tokens - min = {min(output_tokens)}, max = {max(output_tokens)}, mean = {statistics.mean(output_tokens):.2f}, stdev = {statistics.stdev(output_tokens):.2f}")


assert len(output_tokens) == N and all(n > 0 for n in output_tokens), "output_tokens 应大于 0"
print("测试通过！")
print("token 数会受tokenizer的影响；不要只按字数推算，也不要预设某种语言一定较多")
