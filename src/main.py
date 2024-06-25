
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Controllers.apple_music_import_controller import AppleMusicImportController

def main():
    chrome_profile_path = "C:\\Users\\{UserName}\\AppData\\Local\\Google\\Chrome\\User Data\\{ProfileName}"
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={chrome_profile_path}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://music.apple.com/us/browse");
    time.sleep(5)

    try:
        apple_music_controller = AppleMusicImportController(driver)
        search_bar_element = apple_music_controller.get_search_bar_element()
        WebDriverWait(driver, 10).until(EC.visibility_of(search_bar_element))
        search_bar_element.click()
        sleep(15)
    except NoSuchElementException:
            print("Element not found with all provided locators.")

if __name__ == "__main__":
    main()