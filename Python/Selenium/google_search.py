from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


search_text = input("What would you like to search in google?: ")

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com/")
driver.maximize_window()

search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_bar.send_keys(search_text)
search_bar.send_keys(Keys.RETURN)


