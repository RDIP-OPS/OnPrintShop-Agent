import requests
from bs4 import BeautifulSoup
import os

os.makedirs("onprintshop_docs", exist_ok=True)

urls = [
    "https://support.onprintshop.com/en/support/solutions/articles/44002248632-getting-started",
    "https://support.onprintshop.com/en/support/solutions/articles/44002248854-setting-up-products"
]

for url in urls:
    print(f"Scraping: {url}")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text(separator='\n')
    filename = url.split("/")[-1].replace("-", "_") or "index"
    with open(f"onprintshop_docs/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

print("✅ Done scraping!")

