import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class Information_Page:
    _FIRST_NAME=(By.ID,'first-name')
    _LAST_NAME=(By.ID,'last-name')
    _POST_CODE=(By.ID,'postal-code')
    _CONTINUE_BUTTON=(By.ID,'continue')

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def fill_info(self, first_name, last_name, postal_code):
        time.sleep(2)

        fn = self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME))
        ln = self.wait.until(EC.visibility_of_element_located(self._LAST_NAME))
        pc = self.wait.until(EC.visibility_of_element_located(self._POST_CODE))

        actions = ActionChains(self.driver)

        actions.move_to_element(fn).click().send_keys(first_name).pause(0.5) \
            .move_to_element(ln).click().send_keys(last_name).pause(0.5) \
            .move_to_element(pc).click().send_keys(postal_code).perform()

        time.sleep(1)

    def click_continue(self):
        btn = self.wait.until(EC.presence_of_element_located(self._CONTINUE_BUTTON))

        self.driver.execute_script("arguments[0].click();", btn)

        try:
            self.wait.until(EC.url_contains("step-two"))
        except TimeoutException:
            self.driver.save_screenshot("despair_screenshot.png")
            raise
