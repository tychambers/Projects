# This script pulls the daily quote from the below website
# Only tested this with one day, so format may change depending on if changes are made on the site

import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.insightoftheday.com/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the paragraph tags

author = soup.find("div", attrs={"class": "quote"})

author_text = author.text
author_text1 = author_text.split('"')[0]

# the motivational quote is embedded in an image, pulling the alt tag which has the quote
images = soup.find_all("img")
quote_text = images[4].get('alt')
quote_text1 = quote_text.split('</span>')
quote_text2 = quote_text1[1].split('</p>')

print(quote_text2[0])
print(author_text1)






