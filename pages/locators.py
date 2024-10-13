from selenium.webdriver.common.by import By

class Locators:
    """MAIN PAGE"""
    resources = By.ID, 'navitem_about'
    contacts_button = By.ID, 'navitem_about_contacts'

    """CONTACTS PAGE"""
    contacts_title = By.XPATH ,'//*[@class="h1mid"]'
    offices = By.XPATH ,'//div[contains(@class,"companydata")]'

    """CSS Selectors"""
    office_region = 'span.region[itemprop="addressLocality"]'
    company_name = 'span > b'
    address_country = 'span[itemprop="addressCountry"]'
    street_address = 'span[itemprop="streetAddress"]'
    postal_code = 'span[itemprop="postalCode"]'
    telephone = 'span[itemprop="telephone"]'
