# Copyright © 2024 Tüm Hakları Saklıdır.
# Developer: Onur KÖSE
# Nick Name: MrRadar

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get('https://music.apple.com/tr/search')
print(driver.title)

songTitle = "mor ve ötesi bir derdim var"

search_bar = driver.find_element(By.CSS_SELECTOR, "input[class='search-input__text-field svelte-x37dhv']")
search_bar.send_keys(songTitle)
search_bar.send_keys(Keys.RETURN)

button_opt = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='contextual-menu__trigger']")))
button_opt.click()

button_opt = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[title='View Credits']")))
button_opt.click()

preview_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class='click-action svelte-jc0czi']")))
preview_button.click()
sleep(15)
