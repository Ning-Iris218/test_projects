from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout_Overview:
    _FIN_BUTTON=(By.ID,'finish')
    _TITLE=(By.CLASS_NAME,'title')

    def __init__(self,driver):
        self.driver = driver

    def click_finish(self):
        print(f"当前在结算预览页，网址: {self.driver.current_url}")
        wait = WebDriverWait(self.driver, 10)
        finish_btn=wait.until(EC.presence_of_element_located(self._FIN_BUTTON))
        self.driver.execute_script('arguments[0].click();', finish_btn)


    def get_complete(self):
        text=self.driver.find_element(*self._TITLE).text
        return text