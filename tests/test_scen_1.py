from pages.main_page import MainSbisPage
from pages.tensor_page import TensorPage


def test_scenario_1(browser):
    page_contacts = MainSbisPage(browser)
    page_contacts.go_main_page()  # Переходим на страницу sbis
    page_contacts.go_to_contacts()  # Переход на страницу контактов
    page_contacts.go_logo_link()  # Переход по баннеру Tensor

    page_tensor = TensorPage(browser)
    page_tensor.power_in_people_check() # Проверяем наличия текста "Сила в людях"
    page_tensor.go_page_power_in_people()  # Переход на страницу "Сила в людях"
    page_tensor.tensor_page_check()  # Проверка, что мы на корректной странице
    page_tensor.check_picture_on_page()  # Проверка размеров изображения, как пример берутся значения первого и проверяются остальные
