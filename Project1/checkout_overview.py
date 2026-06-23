from selenium.webdriver.common.by import By

class Checkout_Overview:
    _FIN_BUTTON=(By.ID,'finish')
    _TITLE=(By.CLASS_NAME,'title')

    def __init__(self,driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element(*self._FIN_BUTTON).click()

    def get_complete(self):
        text=self.driver.find_element(*self._TITLE).text
        return text