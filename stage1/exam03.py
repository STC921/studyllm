import sys, time
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

latencies = []
output_tokens = []
for _ in range(5):
    t0 = time.time()
    r = client.chat.completions.create(
        model="qwen3.8:27b",
        max_tokens=200,
        messages=[
            {"role": "user", "content": "こんにちは！簡単に自己紹介してください。"},
        ],
    )
    latencies.append(time.time() - t0)
    output_tokens.append(r.usage.completion_tokens)

avg_latency = sum(latencies) / len(latencies)
out_tok_avg = sum(output_tokens) / len(output_tokens)
tps = out_tok_avg / avg_latency if avg_latency > 0 else 0

print(f"model: qwen3.8:27b")
print(f"5 回 latency (sec): min={min(latencies):.2f} max={max(latencies):.2f} mean={avg_latency:.2f}")
print(f"avg output: {out_tok_avg} tokens、大体 {tps:.1f} tokens/sec")
print(f"\n1000 回のコスト: $0 (ローカル)、予定時間: {avg_latency * 1000 / 60:.1f} 分")

assert avg_latency > 0
assert out_tok_avg > 0
print(f"\nテスト通過！ローカルでの推論は無料ですが 1000 回の処理には {avg_latency * 1000 / 60:.1f} 分かかります。")
