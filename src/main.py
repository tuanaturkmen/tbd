
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from Controllers.apple_music_import_controller import AppleMusicImportController

def main():
    driver = webdriver.Chrome();
    driver.get("https://music.apple.com/us/browse");

    try:
        apple_music_controller = AppleMusicImportController(driver)
        search_bar_element = apple_music_controller.get_search_bar_element()
        WebDriverWait(driver, 10).until(EC.visibility_of(search_bar_element));
        search_bar_element.click();
        sleep(15)
    except NoSuchElementException:
            print("Element not found with all provided locators.")



if __name__ == "__main__":
    main()