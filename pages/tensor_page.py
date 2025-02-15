import time

from .base_page import BasePage
from selenium.webdriver.common.by import By

LINK_PAGE_IN_POWER = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-link")
TEXT_PEOPLE_IN_POWER = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-Index__card-title")
PICTURE_ON_PAGE = (By.CSS_SELECTOR, ".tensor_ru-About--col-md6 img")


class TensorPage(BasePage):

    def go_page_power_in_people(self):
        link_go = self.find_element_EC(LINK_PAGE_IN_POWER)
        link_go.click()

    def tensor_page_check(self):
        assert self.browser.current_url == "https://tensor.ru/about", "Страница не соответствует адресу https://tensor.ru/about"

    def power_in_people_check(self):
        time.sleep(1)
        power_in_page = self.find_element_EC(TEXT_PEOPLE_IN_POWER)
        assert power_in_page.text == "Сила в людях", "Текст отличается от 'Сила в людях'"

    def check_picture_on_page(self):
        images = self.find_elements_EC(PICTURE_ON_PAGE) # Находим элементы изображений на странице

        size_first_image = (images[0].size["width"], images[0].size["height"]) # Узнаем размер первого изображения

        for image in images[1:]: # Проходимся по списку найденных изображений и проверяем что они одного размера
            assert (image.size["width"], image.size["height"]) == size_first_image, "Размер картинок отличается"
