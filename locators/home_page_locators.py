from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_UP = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_STATUS_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Статус заказа']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    LOGO_YANDEX = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
    LOGO_SCOOTER = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def faq_answer(index):
        return (By.ID, f"accordion__panel-{index}")