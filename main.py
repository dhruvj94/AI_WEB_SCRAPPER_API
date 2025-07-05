import streamlit as st
from scrape import scrape_website
from scrape1 import scrape_website1
from scrape2 import scrape_website2

st.title("AI Web Scraper")
url = st.text_input("Enter website URL: ")

if st.button("Scrape Site:"):
    st.write("Scraping the website")

    result = scrape_website2(url)
    print(result)