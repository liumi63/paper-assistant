import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# 从环境变量中获取 API 密钥
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("请设置 OPENAI_API_KEY 环境变量。")

# 初始化客户端
client = OpenAI(api_key=api_key)

# 简单测试：让模型生成一句话
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "你好，帮我生成一句测试用的中文问候语"}]
)

print(resp.choices[0].message.content)