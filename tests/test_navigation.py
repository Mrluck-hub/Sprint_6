import allure
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Проверка логотипа Яндекса (редирект на Дзен)")
    def test_logo_yandex(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.click_element(HomePageLocators.LOGO_YANDEX)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 15).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url

    @allure.title("Проверка логотипа Самоката (возврат на главную)")
    def test_logo_scooter(self, driver):
        home = HomePage(driver)
        home.open_home()
        home.click_element(HomePageLocators.ORDER_BUTTON_UP)
        home.click_element(HomePageLocators.LOGO_SCOOTER)
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru"