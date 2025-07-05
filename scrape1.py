from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


def scrape_website1(website):
    print("Launching Chorme brouser... ")

    chrome_driver_path= "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)

    try:
        driver.get(website)
        print("Page loaded.. ")
        html = driver.page_source
        time.sleep(10)
        with open("website.html", "w", encoding="utf-8") as file:
            file.write(html)
        
        website = pd.read_html("website.html")
        new = website[0].dropna()  # Remove NaN rows
        with open("good1.txt", "w", encoding="utf-8") as file:
            file.write(new.to_string(index=False, header=False))
            
        # Print the number of tables found and their content
        print(f"Found {len(website)} tables")
        for i, table in enumerate(website):
            print(f"Table {i}:\n{table}\n")
        print("Scraping completed successfully.")
        new2 = website[2]  # Example: second table
        
        return new2

    finally:
        driver.quit()