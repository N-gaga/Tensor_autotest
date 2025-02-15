from pages.contacts_page import ContactsPage
from pages.main_page import MainSbisPage


def test_scenario_2(browser):
    page_contacts = MainSbisPage(browser)
    page_contacts.go_main_page() # Переходим на страницу sbis
    page_contacts.go_to_contacts()  # Переход на страницу контактов

    page_contacts = ContactsPage(browser)
    page_contacts.check_region("Свердловская обл.") # Проверяем регион на странице с указанным здесь
    page_contacts.check_partner_list() # Проверяем наличие списка партнеров
    page_contacts.change_region() # Меняем регион
    page_contacts.check_region() # Также проверяем регион, но здесь проверяется регион указанный по умолчанию в самом действии
