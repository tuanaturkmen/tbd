from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from ElementIdentifiers import ElementIdentifiers
from time import sleep

#function to find the needed web element 
def find_browser_element(driver, primary_id, *other_ids):
    try:
        primary_element = driver.find_element(*primary_id)

        for by_id, value in other_ids:
            elements = driver.find_elements(by_id, value)
            if primary_element not in elements:
                raise NoSuchElementException(f"Element not matching locator: ({by_id}, {value})")
        return primary_element
    
    except NoSuchElementException as e:
        print(f"Error: {e}")
        raise
#############################################################



#main flow
driver = webdriver.Chrome(); #Initializes Chrome WebDriver
driver.get("https://music.apple.com/us/browse"); #Navigates to given url with specified browser

try:
    primary_identifier = (By.ID, ElementIdentifiers.id_apple_music_search);
    other_identifiers = [
        (By.CLASS_NAME, ElementIdentifiers.class_apple_music_search),
        (By.CSS_SELECTOR, ElementIdentifiers.selector_apple_music_search)
    ]

    search_bar_element = find_browser_element(driver, primary_identifier, *other_identifiers);

    WebDriverWait(driver, 10).until(EC.visibility_of(search_bar_element));
    search_bar_element.click();

    sleep(15)
    

except NoSuchElementException:
        print("Element not found with all provided locators.")






#primary_identifier = (By.ID, ElementIdentifiers.id_apple_music_search);
#other_identifiers = [
#        (By.CLASS_NAME, ElementIdentifiers.class_apple_music_search),
#        (By.CLASS_NAME, ElementIdentifiers.class_apple_music_search)
       # (By.CSS_SELECTOR, ElementIdentifiers.selector_apple_music_search)
 #   ]

  #  search_bar_element = find_browser_element(driver, primary_identifier, other_identifiers);