import os
import csv

from base.base_class import Base
from pages.locators import Locators
from utils.constants import Constants


class ContactsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def parse_office(self):
        self.get_current_url()
        arr = self.search_elements(Locators.offices)
        with open(Constants.file_name, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';')
            csvwriter.writerow(['Country', 'CompanyName', 'FullAddress'])
            for block in arr:

                country = self.find_element_and_get_text_by_css(block, Locators.office_region)
                company_name = self.find_element_and_get_text_by_css(block, Locators.company_name)
                if not country or not company_name:
                    continue
                full_address = ""
                full_address += self.find_element_and_get_text_by_css(block, Locators.address_country)
                full_address += self.find_element_and_get_text_by_css(block, Locators.street_address)
                full_address += self.find_element_and_get_text_by_css(block, Locators.postal_code)
                full_address += self.find_element_and_get_text_by_css(block, Locators.telephone)

                csvwriter.writerow([country, company_name, full_address.strip(", ")])



        """Проверка"""
        assert os.path.exists(Constants.file_name), "CSV файл не был создан"

        with open(Constants.file_name, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')

            rows = list(csvreader)
            assert len(rows) > 1

            # Проверка первой строки с данными
            assert rows[1][0], "Страна не может быть пустой"
            assert rows[1][1], "Название компании не может быть пустым"
            assert rows[1][2], "Адрес должен быть заполнен"