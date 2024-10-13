import time

from base.base_class import Base
from pages.locators import Locators
from utils.constants import Constants

class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def click_contacts(self):
        self.get_current_url()
        self.hover_on_element(Locators.resources)
        self.click_element(Locators.contacts_button)
        self.assert_is(Locators.contacts_title, Constants.contacts_title)
        self.assert_url(Constants.contacts_url)