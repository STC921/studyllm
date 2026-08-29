import sys
from pathlib import Path

import yaml
from openai import OpenAI

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

data_path = Path(__file__).parent / "data.yaml"
with open(data_path, encoding="utf-8") as f:
    cases = yaml.safe_load(f)["cases"]

document = [case["text"] for case in cases]
True_Answer = [case["label"] for case in cases]

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

for few_shot in [False, True]:

    Answer = []

    few_shot_examples = """
        例子：
        我想取消我的订阅。
        输出：billing
        应用程序在启动时崩溃。
        输出：bug
        可以更改我的密码吗？
        输出：other
        """ if few_shot else ""

    for i in range(len(document)):

        prompt = f"""
        目标：把客服留言分到 billing、bug 或 other。
        资料：<input_data>
        {document[i]}
        </input_data>
        规则：只根据资料分类；不知道时选 other。
        {few_shot_examples}
        输出：只回一个小写的标签。
        """

        message = client.chat.completions.create(
            model="qwen3.8:27b",
            temperature=1,
            messages=[
                {"role": "user", "content": prompt},
            ],
        )

        Answer.append(message.choices[0].message.content)

    accuracy = sum(1 for i in range(len(Answer)) if Answer[i] == True_Answer[i]) / len(Answer)
    print(f"few_shot={few_shot} 预测正确率:", accuracy)


