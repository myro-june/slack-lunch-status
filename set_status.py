import requests
import os
import time
from datetime import datetime

# 화요일(Tuesday)은 실행하지 않음 (weekday() == 1)
if datetime.now().weekday() == 1:
          print("오늘은 화요일이라 상태를 변경하지 않습니다.")
          exit(0)

SLACK_TOKEN = os.environ["SLACK_TOKEN"]

expiration = int(time.time()) + (90 * 60)  # 현재시각 + 90분(1시간30분)

payload = {
          "profile": {
                        "status_text": "식사중",
                        "status_emoji": ":rice:",
                        "status_expiration": expiration
          }
}

response = requests.post(
          "https://slack.com/api/users.profile.set",
          headers={"Authorization": f"Bearer {SLACK_TOKEN}"},
          json=payload
)
print(response.json())
