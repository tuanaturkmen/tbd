
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils.ElementIdentifiers import *


class AppleMusicImportController:


    def __init__(self, driver):
        self.driver = driver


    def find_browser_element(self, primary_id, *other_ids):
        """
        function to find the needed web element 
        """
        try:
            primary_element = self.driver.find_element(*primary_id)

            for by_id, value in other_ids:
                elements = self.driver.find_elements(by_id, value)
                if primary_element not in elements:
                    raise NoSuchElementException(f"Element not matching locator: ({by_id}, {value})")
            return primary_element
        
        except NoSuchElementException as e:
            print(f"Error: {e}")
            raise


    def get_search_bar_element(self):
        primary_identifier = (By.ID, id_apple_music_search);
        other_identifiers = [
            (By.CLASS_NAME, class_apple_music_search),
            (By.CSS_SELECTOR, selector_apple_music_search)
        ]

        search_bar_element = self.find_browser_element(primary_identifier, *other_identifiers);
        return search_bar_element
