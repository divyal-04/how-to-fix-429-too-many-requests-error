# 🚫 429 Too Many Requests — Naive vs Smart HTTP Requests

This repository demonstrates a **very common mistake** made while web scraping or automating websites — making **naive HTTP requests** without proper headers.

Using Reddit as an example, we compare:
- ❌ A naive request (likely to get blocked or rate-limited)
- ✅ A smarter request that mimics a real browser

---

## ❌ Naive Method (What NOT to do)

```python
import requests

r = requests.get("https://old.reddit.com")

html = r.text
title = html.split("<title>")[1].split("</title>")[0].strip()

print("Status code:", r.status_code)
print("Page title:", title)
