import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators

@allure.feature("Заказ")
class TestOrder:
    @allure.title("Заказ через точку входа: {entry_name}")
    @pytest.mark.parametrize("btn, entry_name, name, surname, addr, phone, date", [
        (HomePageLocators.ORDER_BUTTON_UP, "Верхняя кнопка", "Кубик", "Кубиков", "Мира 1", "89991112233", "20.10.2026"),
        (HomePageLocators.ORDER_BUTTON_BOTTOM, "Нижняя кнопка", "Круглик", "Кругликов", "Ленина 5", "89001112233", "21.10.2026")
    ])
    def test_order_flow(self, driver, btn, entry_name, name, surname, addr, phone, date):
        home, order = HomePage(driver), OrderPage(driver)
        home.open_home()
        home.accept_cookies()
        home.scroll_to_element(btn)
        home.click_element(btn)
        order.make_order(name, surname, addr, phone, date)
        assert "Заказ оформлен" in order.find_element(OrderPageLocators.SUCCESS_ORDER_TITLE).text