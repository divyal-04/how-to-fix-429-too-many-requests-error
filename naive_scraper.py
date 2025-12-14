import requests

r = requests.get("https://old.reddit.com")

html = r.text
title = html.split("<title>")[1].split("</title>")[0].strip()

print("Status code:", r.status_code)
print("Page title:", title)