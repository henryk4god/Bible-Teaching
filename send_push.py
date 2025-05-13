import requests
import json
import datetime
import os

# Load secrets from GitHub Actions
APP_ID = os.environ.get("ONESIGNAL_APP_ID")
API_KEY = os.environ.get("ONESIGNAL_API_KEY")

# Create dynamic title & message
today = datetime.datetime.now().strftime("%A, %d %B")
title = f"Daily Inspiration {today}"
message = "Click to read today’s teaching and prayer points 🙏"

# Payload
payload = {
    "app_id": APP_ID,
    "included_segments": ["Subscribed Users"],
    "headings": {"en": title},
    "contents": {"en": message},
    "url": "https://mofoluwakeedgar.com/bible-study/"  # Change this
}

# Send push
res = requests.post(
    "https://onesignal.com/api/v1/notifications",
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {API_KEY}"
    },
    data=json.dumps(payload)
)

print(f"Status: {res.status_code}")
print(f"Response: {res.json()}")