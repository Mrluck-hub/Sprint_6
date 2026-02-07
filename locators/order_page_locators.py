from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    METRO_STATION_OPTION = (By.XPATH, ".//button[@value='1']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    RENT_PERIOD_DAY = (By.XPATH, ".//div[text()='сутки']")
    ORDER_FINAL_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_ORDER_TITLE = (By.XPATH, ".//div[contains(@class, 'Order_Modal')]")
