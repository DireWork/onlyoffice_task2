import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:

    def __init__(self, driver=None):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Method assert word"""
    def assert_is(self, locator, expected_text):
        element = self.check_element_presence(locator)
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"

    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("good value URL")

    """Method check element presence"""
    def check_element_presence(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element
        except:
            print("Error: element_presence")
            raise

    """Method click element"""
    def click_element(self, locator):
        try:
            element = self.check_element_presence(locator)
            element.click()
            time.sleep(1)
        except:
            print("Error: click_element")
            raise

    def find_element_and_get_text_by_css(self,block, locator):
        try:
            return " ".join([element.text for element in block.find_elements(By.CSS_SELECTOR, locator)])
        except:
            pass

    """Method select in dropdown"""
    def hover_on_element(self, locator):
        try:
            element = self.check_element_presence(locator)
            ActionChains(self.driver).move_to_element(element).perform()
            time.sleep(1)
        except:
            print("Error: hover_on_element")
            raise

    """Method find elements"""
    def search_elements(self, locator):
        try:
            elements = self.driver.find_elements(*locator)
            return elements
        except:
            print("Error: search_elements")
            raise