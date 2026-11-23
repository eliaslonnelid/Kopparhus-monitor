import requests
import os
from datetime import datetime

TOKEN = os.environ["PUSHOVER_TOKEN"]
USER = os.environ["PUSHOVER_USER"]

requests.post(
    "https://api.pushover.net/1/messages.json",
    data={
        "token": TOKEN,
        "user": USER,
        "title": "GitHub Test",
        "message": f"Workflow körd {datetime.now()}"
    },
    timeout=30,
)

print("Pushnotis skickad")
