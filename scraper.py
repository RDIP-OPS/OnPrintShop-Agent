from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import time

# ✅ Your OnPrintShop pages
urls = [
    "https://docs.onprintshop.com/",
    "https://docs.onprintshop.com/user-manual",
    "https://docs.onprintshop.com/latest-solution-releases"
]

# ✅ Setup output folder
os.makedirs("onprintshop_docs", exist_ok=True)

# ✅ Setup headless Chrome
options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

valid_pages = []

for url in urls:
    try:
        print(f"🔍 Fetching: {url}")
        driver.get(url)
        time.sleep(5)  # wait for JS to load

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n").strip()
        word_count = len(text.split())

        if word_count > 30:
            print(f"✅ Valid ({word_count} words): {url}")
            valid_pages.append((url, text))
        else:
            print(f"⚠️ Skipped: Too short ({word_count} words)")

    except Exception as e:
        print(f"❌ Error with {url}: {e}")

driver.quit()

print(f"\n📄 Saving {len(valid_pages)} valid pages...")

for url, text in valid_pages:
    filename = url.split("/")[-1] or "index"
    filename = filename.replace("-", "_")
    with open(f"onprintshop_docs/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)

print("\n✅ Selenium scrape complete!")
