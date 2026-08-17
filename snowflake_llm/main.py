import os
import requests
from dotenv import load_dotenv

load_dotenv()

account = os.environ["SNOWFLAKE_ACCOUNT"]
pat = os.environ["SNOWFLAKE_PAT"]
model_name = os.environ["MODEL"]

url = f"https://{account}.snowflakecomputing.com/api/v2/cortex/v1/chat/completions"

response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {pat}",
        "Content-Type": "application/json",
    },
    json={
        "model": model_name,                # ✅ variable, not a string literal
        "messages": [{"role": "user", "content": "What is best approach for agent memory using llms?"}],
    },
)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")
else:
    data = response.json()
    print(data["choices"][0]["message"]["content"])