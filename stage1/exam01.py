import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

r = client.chat.completions.create(
    model="qwen3.8:27b",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "用一句话自我介绍。"},
    ],
)

text = r.choices[0].message.content
print("响应：", text)
print("usage:", r.usage)

assert r.choices[0].finish_reason in ("stop", "length"), f"非预期 finish_reason: {r.choices[0].finish_reason}"
assert len(text) > 0, "响应不应为空"
assert r.usage.completion_tokens > 0, "completion_tokens 应大于 0"
print("测试通过！")