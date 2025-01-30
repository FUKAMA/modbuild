import os
import json
from openai import OpenAI

# シンプルなメッセージを送信し結果を受け取る
def SimnpleMessage(msg,gptModel="gpt-4o-mini"):
    # APIキーの設定
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = [{"role": "system","content": "日本語で返答してください。"}]

    prompt.append({"role": "user", "content": str(msg)})

    # OpenAIに問い合わせてプロンプトを送信し結果を受け取る
    result = client.chat.completions.create(
        model=gptModel,
        messages=prompt
    )

    # 結果を返す
    return result.choices[0].message.content