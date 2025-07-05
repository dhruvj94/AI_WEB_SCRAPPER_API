from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

from bs4 import BeautifulSoup


def scrape_website3(website):
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
        
        website_ = pd.read_html("website.html")       
        new = website_[2]  # Example: second table
        print(f"Found table3:\n{new}\n")
        
        # Parse HTML with BeautifulSoup for table names
        soup = BeautifulSoup(website, "html.parser")
        tables = soup.find_all("table")
        captions = [t.find_previous("caption") or t.find_previous("h2") or {"text": f"Table {i+1}"} for i, t in enumerate(tables)]
        
        # Write all tables to good2.txt with clear separation
        with open("good3.txt", "w", encoding="utf-8") as file:
            for i, table in enumerate(website_):
                caption_text = captions[i]["text"] if isinstance(captions[i], dict) else captions[i].get_text(strip=True)
                file.write(f"\n=== Table {i + 1}: {caption_text} (Columns: {', '.join(table.columns)}) ===\n")
                table = table.dropna(how="all")  # Remove fully empty rows
                file.write(table.to_string(index=False, header=False))
                file.write("\n\n")  # Add spacing between tables
            
        return new

    finally:
        driver.quit()