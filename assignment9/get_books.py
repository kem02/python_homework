from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)

try:

    driver.get(
        "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    )

    title = driver.title
    print(title)

    lists = driver.find_elements(By.CSS_SELECTOR, ".cp-search-result-item")

    results = []

    for list in lists:

        title = list.find_element(By.CLASS_NAME, "title-content").text
        # print(title)

        authors = [
            author.text
            for author in list.find_elements(
                By.CSS_SELECTOR, ".cp-author-link .author-link"
            )
        ]

        if len(authors) > 1:
            authors = ";".join(authors)
        else:
            authors = authors[0]
        # print(authors)

        format = list.find_element(
            By.CSS_SELECTOR, ".cp-format-info .display-info-primary"
        ).text
        # print(format)

        data = {"Title": title, "Author": authors, "Format-Year": format}
        results.append(data)

        # print(results)

        df = pd.DataFrame(results)
        # print(df)


except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()


df.to_csv("./get_books.csv", index=False)

with open("./get_books.json", "w", newline="") as json_file:
    json.dump(results, json_file, indent=4)
