import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ищем элемент {locator}")
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step("Ищем список элементов {locator}")
    def find_elements_list(self, locator, time=5):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
        except:
            return []

    @allure.step("Кликаем на элемент {locator}")
    def click_element(self, locator):
        self.scroll_to_element(locator)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Прокручиваем к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получаем текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text    

    @allure.step("Вводим текст в поле {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ждем, пока URL будет содержать {text}")
    def wait_url_contains(self, text):
        return WebDriverWait(self.driver, 15).until(EC.url_contains(text))

    @allure.step("Получаем текущий URL")
    def current_url(self):
        return self.driver.current_url
        