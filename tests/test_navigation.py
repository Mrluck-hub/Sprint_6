import allure
from pages.home_page import HomePage
from curl import URL_HOME

@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Проверка логотипа Яндекса (редирект на Дзен)")
    def test_logo_yandex(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.click_yandex_logo()
        home.switch_to_new_tab()
        assert home.wait_url_contains("dzen.ru")

    @allure.title("Проверка логотипа Самоката (возврат на главную)")
    def test_logo_scooter(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.click_order_button("up")
        home.click_scooter_logo()
        assert home.current_url() == URL_HOME + "/"