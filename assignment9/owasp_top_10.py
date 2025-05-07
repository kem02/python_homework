from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

# Task 6
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)


try:
    driver.get("https://owasp.org/www-project-top-ten/")

    title = driver.title
    print(title)

    section_parent = driver.find_element(By.CSS_SELECTOR, "#sec-main")
    # print(section_parent.text)

    section_ul = section_parent.find_element(By.XPATH, "./ul[last()]")
    # print(section_ul.text)

    results = []

    lists = section_ul.find_elements(By.CSS_SELECTOR, "a")
    for list in lists:
        title = list.find_element(By.CSS_SELECTOR, "strong").text
        # print(title)

        link = list.get_attribute("href")
        # print(link)

        data = {"vulnerability_title": title, "link": link}
        results.append(data)

    print(results)


except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()


with open("./owasp_top_10.csv", "w", newline="") as file:

    fieldnames = ["vulnerability_title", "link"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
