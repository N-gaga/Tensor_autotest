from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def find_element_EC(self, locator):  # Действие поиска элемента с явным ожидаем
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements_EC(self, locator):  # Действие поиска элементов с явным поиском ожидания
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_EC(self, locator): # Ожидание, когда объект станет кликабельным и уже после использовать клик
        self.wait.until(EC.element_to_be_clickable(locator)).click()
