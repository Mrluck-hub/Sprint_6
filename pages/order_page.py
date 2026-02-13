import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    @allure.step("Заполняем форму заказа")
    def make_order(self, name, surname, address, phone, date):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.click_element(OrderPageLocators.METRO_STATION_OPTION)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.find_element(OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)
        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.RENT_PERIOD_DAY)
        self.click_element(OrderPageLocators.ORDER_FINAL_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Получаем текст успешного заказа")
    def get_success_title(self):
        return self.get_text(OrderPageLocators.SUCCESS_ORDER_TITLE)