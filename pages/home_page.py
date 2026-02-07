import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    @allure.step("Открываем главную страницу")
    def open_home(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru")

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        if self.driver.find_elements(*HomePageLocators.COOKIE_BUTTON):
            self.click_element(HomePageLocators.COOKIE_BUTTON)

    @allure.step("Кликаем на вопрос FAQ №{index}")
    def click_faq_question(self, index):
        locator = HomePageLocators.faq_question(index)
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Получаем текст ответа FAQ №{index}")
    def get_faq_answer_text(self, index):
        return self.find_element(HomePageLocators.faq_answer(index)).text