# Web scraping is the process of collecting and parsing raw data from the Web,

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
# The find_all method is used for finding out all tags with the specified tag name or id and returning them as a list of type bs4.
quotes = soup.find_all("span", class_= "text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_= "tags")

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all("a", class_="tag")

    for quoteTag in quoteTags:
        print(quoteTag.text)
