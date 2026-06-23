from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Information_Page:
    _FIRST_NAME=(By.ID,'first-name')
    _LAST_NAME=(By.ID,'last-name')
    _POST_CODE=(By.ID,'postal-code')
    _CONTINUE_BUTTON=(By.ID,'continue')

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def fill_info(self,first_name,last_name,postal_code):
        self.wait.until(EC.presence_of_element_located(self._FIRST_NAME)).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located(self._LAST_NAME)).send_keys(last_name)
        self.wait.until(EC.presence_of_element_located(self._POST_CODE)).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
