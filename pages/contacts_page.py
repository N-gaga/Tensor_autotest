import time

from .base_page import BasePage
from selenium.webdriver.common.by import By

LIST_PARTNER = (By.ID, "city-id-2")
REGION_AFTER_CONTACTS = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser.ml-16 .sbis_ru-Region-Chooser__text")
LINK_KAMCHATKA_REGION = (By.XPATH, '//span[@title="Камчатский край"]')


class ContactsPage(BasePage):

    def check_region(self, name_region="Камчатский край"): # Проверка и пример задания региона по умолчанию
        time.sleep(0.5) # Есть какая-то проблема, что явное ожидание не помогает, поставил паузу
        variable_region_after_contacts = self.find_element_EC(REGION_AFTER_CONTACTS)
        page_name_region = variable_region_after_contacts.text
        assert page_name_region == name_region, "Регионы не совпадают" # Проверка с регионом по умолчанию или указанным в тестовом сценарии

    def check_partner_list(self): # Проверка наличия списка партнеров в регионе
        list_partner_region = self.find_element_EC(LIST_PARTNER)
        assert list_partner_region.is_displayed(), "Список партнёров отсутствует"

    def change_region(self): # Смена региона
        self.find_element_EC(REGION_AFTER_CONTACTS)
        self.click_EC(REGION_AFTER_CONTACTS)
        self.click_EC(LINK_KAMCHATKA_REGION)
