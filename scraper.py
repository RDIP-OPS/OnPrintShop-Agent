from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import time

# ✅ Your OnPrintShop pages - IMPORTANT: Only use public, text-rich URLs
# These URLs are known to work well with Selenium for dynamic content.
urls = [
    "https://docs.onprintshop.com/user-manual",
    "https://docs.onprintshop.com/user-manual/mdrR-introduction",
    "https://docs.onprintshop.com/user-manual/website-themes",
    "https://docs.onprintshop.com/user-manual/ready-to-buy-products",
    "https://docs.onprintshop.com/user-manual/faqs",
    "https://docs.onprintshop.com/user-manual/video-tutorials",
    "https://docs.onprintshop.com/user-manual/add-on-modules",
    "https://docs.onprintshop.com/user-manual/workflow-admin",
    "https://docs.onprintshop.com/user-manual/integrations",
    "https://docs.onprintshop.com/user-manual/third-party-shipping",
    "https://docs.onprintshop.com/user-manual/shipping-cost-by-order-subtotal",
    "https://docs.onprintshop.com/user-manual/manage-forms",
    "https://docs.onprintshop.com/user-manual/latest-releases",
    "https://docs.onprintshop.com/user-manual/custom-size-products",
    "https://docs.onprintshop.com/user-manual/promotional-products",
    "https://docs.onprintshop.com/user-manual/product-settings",
    "https://docs.onprintshop.com/user-manual/links-header-and-footer",
    "https://docs.onprintshop.com/user-manual/language-text-references",
    "https://docs.onprintshop.com/user-manual/sidebar-management",
    "https://docs.onprintshop.com/user-manual/store-setup",
    "https://docs.onprintshop.com/user-manual/store-configurations",
    "https://docs.onprintshop.com/user-manual/rB0I-settings",
    "https://docs.onprintshop.com/user-manual/store-configuration-tab",
    "https://docs.onprintshop.com/user-manual/images-tab",
    "https://docs.onprintshop.com/user-manual/after-login-redirection-tab",
    "https://docs.onprintshop.com/user-manual/content-management",
    "https://docs.onprintshop.com/user-manual/contents",
    "https://docs.onprintshop.com/user-manual/manage-site-access",
    "https://docs.onprintshop.com/user-manual/store-personalization",
    "https://docs.onprintshop.com/user-manual/products",
    "https://docs.onprintshop.com/user-manual/knowing-products",
    "https://docs.onprintshop.com/user-manual/creating-products",
    "https://docs.onprintshop.com/user-manual/add-new-product",
    "https://docs.onprintshop.com/user-manual/managing-products",
    "https://docs.onprintshop.com/user-manual/pricing-setup",
    "https://docs.onprintshop.com/user-manual/product-categories",
    "https://docs.onprintshop.com/user-manual/templates",
    "https://docs.onprintshop.com/user-manual/product-templates",
    "https://docs.onprintshop.com/user-manual/master-templates",
    "https://docs.onprintshop.com/user-manual/pdf-block-templates",
    "https://docs.onprintshop.com/user-manual/designer-studio",
    "https://docs.onprintshop.com/user-manual/general",
    "https://docs.onprintshop.com/user-manual/common-studio-settings",
    "https://docs.onprintshop.com/user-manual/top-panel",
    "https://docs.onprintshop.com/user-manual/duplicate-templates",
    "https://docs.onprintshop.com/user-manual/managing-studio",
    "https://docs.onprintshop.com/user-manual/orders",
    "https://docs.onprintshop.com/user-manual/unpaid-orders",
    "https://docs.onprintshop.com/user-manual/job-board",
    "https://docs.onprintshop.com/user-manual/archive-orders",
    "https://docs.onprintshop.com/user-manual/pattern",
    "https://docs.onprintshop.com/user-manual/viewing-orders",
    "https://docs.onprintshop.com/user-manual/quote-management",
    "https://docs.onprintshop.com/user-manual/add-new-quote",
    "https://docs.onprintshop.com/user-manual/ZAFG-dashboard",
    "https://docs.onprintshop.com/user-manual/quick-actions",
    "https://docs.onprintshop.com/user-manual/printer-quotes",
    "https://docs.onprintshop.com/user-manual/quote-form",
    "https://docs.onprintshop.com/user-manual/flow-of-quote",
    "https://docs.onprintshop.com/user-manual/imposition-beta-version",
    "https://docs.onprintshop.com/user-manual/customers",
    "https://docs.onprintshop.com/user-manual/pcMc-customers",
    "https://docs.onprintshop.com/user-manual/product-schema-settings",
    "https://docs.onprintshop.com/user-manual/website-customers",
    "https://docs.onprintshop.com/user-manual/introduction", # For Business Partners
    "https://docs.onprintshop.com/user-manual/printers",
    "https://docs.onprintshop.com/user-manual/sales-agent",
    "https://docs.onprintshop.com/user-manual/print-store-branch",
    "https://docs.onprintshop.com/user-manual/partners",
    "https://docs.onprintshop.com/user-manual/production-time-spent",
    "https://docs.onprintshop.com/user-manual/knowing-store",
    "https://docs.onprintshop.com/user-manual/creating-store",
    "https://docs.onprintshop.com/user-manual/managing-store",
    "https://docs.onprintshop.com/user-manual/GiNJ-introduction",
    "https://docs.onprintshop.com/user-manual/store-dashboard",
    "https://docs.onprintshop.com/user-manual/marketing",
    "https://docs.onprintshop.com/user-manual/seo",
    "https://docs.onprintshop.com/user-manual/page-title-keyword-setting",
    "https://docs.onprintshop.com/user-manual/sitemaps",
    "https://docs.onprintshop.com/user-manual/metatag-settings",
    "https://docs.onprintshop.com/user-manual/robots",
    "https://docs.onprintshop.com/user-manual/web-optimization",
    "https://docs.onprintshop.com/user-manual/coupon-and-discounts",
    "https://docs.onprintshop.com/user-manual/reward-points",
    "https://docs.onprintshop.com/user-manual/manage-admins",
    "https://docs.onprintshop.com/user-manual/admin",
    "https://docs.onprintshop.com/user-manual/admin-grouprole",
    "https://docs.onprintshop.com/user-manual/common-settings",
    "https://docs.onprintshop.com/user-manual/viewing-reports",
    "https://docs.onprintshop.com/user-manual/reports",
    "https://docs.onprintshop.com/user-manual/cms-blocks-setup",
    "https://docs.onprintshop.com/user-manual/create-idml-file-from-ai-file",
    "https://docs.onprintshop.com/user-manual/custom-art-logo-maker",
    "https://docs.onprintshop.com/user-manual/creating-custom-art-admin",
    "https://docs.onprintshop.com/user-manual/custom-formula-variables",
    "https://docs.onprintshop.com/user-manual/estimated-delivery-days-calculation",
    "https://docs.onprintshop.com/user-manual/generate-content-and-images-using-openai",
    "https://docs.onprintshop.com/user-manual/mass-template-personalization",
    "https://docs.onprintshop.com/user-manual/migration-from-ua-to-ga4",
    "https://docs.onprintshop.com/user-manual/order-cancellation-and-refund",
    "https://docs.onprintshop.com/user-manual/price-calculator-block-setup",
    "https://docs.onprintshop.com/user-manual/quick-product-design",
    "https://docs.onprintshop.com/user-manual/real-preview",
    "https://docs.onprintshop.com/user-manual/reorder-admin-and-front",
    "https://docs.onprintshop.com/user-manual/setup-store-cms-pages",
    "https://docs.onprintshop.com/user-manual/setup-stores-payon-account",
    "https://docs.onprintshop.com/user-manual/solve-email-not-delivered-error",
    "https://docs.onprintshop.com/user-manual/store-fields-use-cases",
    # Original URLs from your script that were not in the document:
    "https://docs.onprintshop.com/getting-started-with-ops",
    "https://onprintshop.com/release-notes/onprintshop-version-12-1",
    "https://onprintshop.com/release-notes",
    "https://onprintshop.com/solutions/web-to-print",
]

# ✅ Setup output folder
os.makedirs("onprintshop_docs", exist_ok=True)

# ✅ Setup headless Chrome (runs Chrome invisibly)
options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

valid_pages = []
print("🚀 Starting dynamic scrape with Selenium...")

for url in urls:
    try:
        print(f"🔍 Fetching: {url}")
        driver.get(url)
        time.sleep(5) # Wait 5 seconds for JavaScript to load content
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n").strip()
        word_count = len(text.split())

        # Filter out pages that don't have enough real text
        if word_count > 30: # Only save if more than 30 words are found
            print(f"✅ Valid ({word_count} words): {url}")
            valid_pages.append((url, text))
        else:
            print(f"⚠️ Skipped (Too short: {word_count} words): {url}")
    except Exception as e:
        print(f"❌ Error with {url}: {e}")

driver.quit() # Close the invisible Chrome browser
print(f"\n📄 Saving {len(valid_pages)} valid pages...")

for url, text in valid_pages:
    filename = url.split("/")[-1] or "index"
    filename = filename.replace("-", "_")
    with open(f"onprintshop_docs/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)
print("\n✅ Selenium scrape complete! Check the 'onprintshop_docs' folder.")
