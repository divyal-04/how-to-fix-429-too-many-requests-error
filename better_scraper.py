import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

r = requests.get("https://old.reddit.com", headers=headers)

html = r.text
title = html.split("<title>")[1].split("</title>")[0].strip()

print("Status code:", r.status_code)
print("Page title:", title)