# Copyright © 2024 Tüm Hakları Saklıdır.
# Developer: Onur KÖSE
# Nick Name: MrRadar

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://music.apple.com/tr/search')
print(driver.title)

search_bar = driver.find_element(By.CSS_SELECTOR, "input[class='search-input__text-field svelte-x37dhv']")
search_bar.send_keys("mor ve ötesi bir derdim var")
print(driver.current_url)
search_bar.send_keys(Keys.RETURN)
sleep(2)
