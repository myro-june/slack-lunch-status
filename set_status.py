import requests
import os
import time

SLACK_TOKEN = os.environ["SLACK_TOKEN"]

expiration = int(time.time()) + (90 * 60)  # 현재시각 + 90분(1시간30분)

payload = {
      "profile": {
                "status_text": "식사중",
                "status_emoji": ":fork_and_knife:",
                "status_expiration": expiration
      }
}

response = requests.post(
      "https://slack.com/api/users.profile.set",
      headers={"Authorization": f"Bearer {SLACK_TOKEN}"},
      json=payload
)
print(response.json())
