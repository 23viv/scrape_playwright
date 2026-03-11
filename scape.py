from playwright.sync_api import sync_playwright
import csv
import time

BASE = "https://vtu.internyet.in"

data = []
links = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # -------- collect company links from all pages --------

    for i in range(1,73):

        url = f"{BASE}/companies?page={i}"
        print("Opening:", url)

        page.goto(url)
        time.sleep(4)

        cards = page.query_selector_all("a[href^='/companies/']")

        for card in cards:

            href = card.get_attribute("href")

            if href:
                links.append(BASE + href)

    # remove duplicates
    links = list(set(links))

    print("Total company links:", len(links))

    # -------- visit company pages --------

    for link in links:

        try:

            page.goto(link)
            time.sleep(3)

            # company name
            name = page.locator("h2").first.inner_text()

            # domain
            domain = page.locator("text=Domain").locator("..").locator("span").first.inner_text()

            # company size
            size_text = page.locator("text=Company Size").inner_text()
            size = size_text.split(":")[-1].strip()

            # location
            spans = page.locator("svg.lucide-map-pin").locator("..").locator("span").all_inner_texts()
            location = ", ".join(spans)

            # year founded
            year = page.locator("text=Year founded").locator("..").locator("p").nth(1).inner_text()

            # website
            website = page.locator("text=Website").locator("..").locator("a").get_attribute("href")

            data.append({
                "name": name,
                "domain": domain,
                "company_size": size,
                "location": location,
                "year_founded": year,
                "website": website
            })

            print("Scraped:", name)

        except Exception as e:
            print("Skipped:", link)

    browser.close()


# -------- save CSV --------

with open("companies.csv","w",newline="",encoding="utf-8") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "name",
            "domain",
            "company_size",
            "location",
            "year_founded",
            "website"
        ]
    )

    writer.writeheader()
    writer.writerows(data)

print("CSV saved!")