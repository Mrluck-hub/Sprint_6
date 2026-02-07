import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем элемент {locator}")
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Кликаем на элемент {locator}")
    def click_element(self, locator):
        self.scroll_to_element(locator)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Прокручиваем к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Вводим текст в поле {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        