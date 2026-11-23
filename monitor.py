import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

URL = "https://kopparhus.se/lediga-objekt/"

TOKEN = os.environ["PUSHOVER_TOKEN"]
USER = os.environ["PUSHOVER_USER"]

STATE_FILE = "seen.json"


def send_push(message):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": TOKEN,
            "user": USER,
            "title": "Ny 4:a hos Kopparhus",
            "message": message
        },
        timeout=30,
    )


try:
    with open(STATE_FILE, "r") as f:
        seen = json.load(f)
except:
    seen = []


html = requests.get(URL, timeout=30).text

soup = BeautifulSoup(html, "html.parser")

text = soup.get_text("\n")

matches = []

for line in text.split("\n"):

    line = line.strip()

    if "4 rok" in line.lower():

        matches.append(line)


for apartment in matches:

    if apartment not in seen:

        send_push(
            f"Ny 4:a hittad!\n\n{apartment}\n\nhttps://kopparhus.se/lediga-objekt/"
        )


# TEST AV SCHEDULER
send_push(
    f"Scheduler test\n\nKördes: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)

with open(STATE_FILE, "w") as f:
    json.dump(matches, f)
