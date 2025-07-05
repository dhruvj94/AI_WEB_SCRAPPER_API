from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


def scrape_website(website):
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
        for line in website:
            new =line
            break
        with open("good.txt", "w", encoding="utf-8") as file:
            file.write(new.to_string(index=False))
        return new
    
    finally:
        driver.quit()