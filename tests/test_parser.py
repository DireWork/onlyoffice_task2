from pages.contacts_page import ContactsPage
from pages.main_page import MainPage

def test_parse_offices(driver):
    main = MainPage(driver)
    main.click_contacts()

    CP = ContactsPage(driver)
    CP.parse_office()
