import requests
from bs4 import BeautifulSoup

zip_code = input("Enter zip code: ")

# Send a GET request to the website
url = f"https://www.google.com/search?q=weather+{zip_code}"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the paragraph tags
try:
    temperature = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
    weather = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"})
    weather_2 = weather.get_text()
    weather_3 = weather_2.split('\n')

    print(f"Weather in {zip_code}:")
    print(f"Date/Time: {weather_3[0]}")
    print(f"Weather: {weather_3[1]}")
    print(f"Temperature: {temperature.text}")

except AttributeError:
    print("Invalid Zip Code try again.")





