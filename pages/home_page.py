import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from curl import URL_HOME

class HomePage(BasePage):
    @allure.step("Открываем главную страницу")
    def open_home(self):
        self.open_url(URL_HOME)

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        if self.driver.find_elements(*HomePageLocators.COOKIE_BUTTON):
            self.click_element(HomePageLocators.COOKIE_BUTTON)

    @allure.step("Нажимаем на кнопку заказа: {button_type}")
    def click_order_button(self, button_type):
        locator = HomePageLocators.ORDER_BUTTON_UP if button_type == "up" else HomePageLocators.ORDER_BUTTON_BOTTOM
        self.click_element(locator)

    @allure.step("Нажимаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(HomePageLocators.LOGO_YANDEX)

    @allure.step("Нажимаем на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.LOGO_SCOOTER)

    @allure.step("Кликаем на вопрос FAQ №{index}")
    def click_faq_question(self, index):
        self.click_element(HomePageLocators.faq_question(index))

    @allure.step("Берем текст ответа FAQ №{index}")
    def get_faq_answer(self, index):
        return self.get_text(HomePageLocators.faq_answer(index))