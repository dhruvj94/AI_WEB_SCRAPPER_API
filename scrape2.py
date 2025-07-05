from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


def scrape_website2(website):
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
        new = website[2]  # Example: second table
        print(f"Found table2:\n{new}\n")
        
        # Write all tables to good2.txt with clear separation
        with open("good2.txt", "w", encoding="utf-8") as file:
            for i, table in enumerate(website):
                file.write(f"\n=== Table {i + 1} ===\n")
                table = table.dropna()  
                file.write(table.to_string(index=False, header=False))
                file.write("\n\n")  # Add spacing between tables
            
        return new

    finally:
        driver.quit()