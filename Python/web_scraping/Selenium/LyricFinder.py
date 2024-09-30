# This App finds lyrics using selenium and google
# type in your favorite song and the name of the artist, and the script will pull that information from google
# and display it on the console

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

song_name = input("What is the name of the song?: ")
band_name = input("What is the name of the band? (If you do not know leave blank): ")

if len(band_name) <= 1:
    search_text = f"{song_name} lyrics"
else:
    search_text = f"{song_name} by {band_name} lyrics"

options = Options()
options.add_experimental_option("detach", True)


# commented below as it stopped working replaced with the line below it
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")
driver.maximize_window()

search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_bar.send_keys(search_text)
search_bar.send_keys(Keys.RETURN)

try:
    song_title = driver.find_element(By.XPATH, "//div[@class = 'PZPZlf ssJ7i B5dxMb']")
    artist_name = driver.find_element(By.XPATH, "//div[@class = 'iAIpCb PZPZlf']")
    lyrics = driver.find_element(By.XPATH, "//div[@jsname = 'WbKHeb']")
    print(song_title.text + "\n")
    print(artist_name.text + "\n")
    print(lyrics.text)
except NoSuchElementException:
    print("We could not find lyrics to that song, please try again.")
