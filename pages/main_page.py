import os
import re
import time
import wget

from .base_page import BasePage
from selenium.webdriver.common.by import By

MAIN_SBIS_PAGE = "https://sbis.ru/"
CONTACT_LIST = (By.CLASS_NAME, "sbis_ru-Header__menu-link")
CONTACT_MORE_OFFICE_LINK = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__items a.sbisru-link")
LOGO_LINK = (By.CSS_SELECTOR, ".sbisru-Contacts__border-left--border-xm a")
LINK_PAGE_DOWNLOAD_LOCAL = (By.XPATH, '//a[@href="/download"]')
LINK_DOWNLOAD_FILE = (By.XPATH, '//a[@href="https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
FILE_NAME = 'sbisplugin-setup-web.exe'


class MainSbisPage(BasePage):

    def go_main_page(self): # Открытие основной страницы
        self.browser.get(MAIN_SBIS_PAGE)

    def go_to_contacts(self): # Переход на страницу контактов
        self.find_element_EC(CONTACT_LIST)
        self.click_EC(CONTACT_LIST)

        self.find_element_EC(CONTACT_MORE_OFFICE_LINK)
        self.click_EC(CONTACT_MORE_OFFICE_LINK)

    def go_logo_link(self): # Переход по баннеру тензор
        self.find_element_EC(LOGO_LINK)
        self.click_EC(LOGO_LINK)
        tensor_window = self.browser.window_handles[1]
        self.browser.switch_to.window(tensor_window)

    def go_link_download_local_versions(self):
        time.sleep(0.5) # Если сразу делать проверку то явное ожидание тоже не срабатывает
        self.find_element_EC(LINK_PAGE_DOWNLOAD_LOCAL)
        self.click_EC(LINK_PAGE_DOWNLOAD_LOCAL)

    def check_page_plugin_windows(self):
        time.sleep(1) # Изначально страница програжуется без параметров по умолчанию, они вставляются в строку чуть позже, явное ожидание не поможет, нужна пауза
        current_url = self.browser.current_url
        assert "plugin" in current_url and "default" in current_url, "Страница открыта не для плагина Windows"

    def download_plugin_and_check(self):

        text_name_file = self.find_element_EC(LINK_DOWNLOAD_FILE)
        text_name_file = text_name_file.text
        text_name_file = float(re.search(r'\d+\.\d+', text_name_file).group()) # Получение указанного числа размера на странице

        wget.download('https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe')
        file_size = os.path.getsize(FILE_NAME)
        file_size = file_size / 1024 / 1024
        try:
            assert (file_size - text_name_file) < 0.01, "Размер файлов не совпадает" # Проверка с погрешностью, т.к. размеры с плавающей точкой
        finally:
            os.remove(FILE_NAME) # Удаление файлов в любом случае чтобы не забивать папку копиями
