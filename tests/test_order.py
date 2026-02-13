import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import ORDER_UP_BOTTON

@allure.feature("Заказ")
class TestOrder:
    @allure.title("Заказ через точку входа: {entry_name}")
    @pytest.mark.parametrize("btn, entry_name, name, surname, addr, phone, date", ORDER_UP_BOTTON)
    def test_order_flow(self, driver, btn, entry_name, name, surname, addr, phone, date):
        home, order = HomePage(driver), OrderPage(driver)
        home.open_home()
        home.accept_cookies()
        home.click_order_button(btn)
        order.make_order(name, surname, addr, phone, date)
        assert "Заказ оформлен" in order.get_success_title()