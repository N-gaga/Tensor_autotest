from pages.main_page import MainSbisPage


def test_scenario_3(browser):
    page = MainSbisPage(browser)
    page.go_main_page() # Переходим на страницу sbis
    page.go_link_download_local_versions() # Переходим на страницу с файлами
    page.check_page_plugin_windows() # Проверяем что открыта нужная страница платформы и файла
    page.download_plugin_and_check() # Скачиваем файл, проверяем соответствие размеров на сайте и в живую, удаляем файл