from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

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
        try:
            btn = self.driver.find_element(*self._CONTINUE_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(0.5)
            btn.click()
            self.wait.until(EC.url_contains("step-two"))

        except TimeoutException:
            self.driver.save_screenshot("github_error_screenshot.png")
            print("🚨 警告：等待跳转 step-two 超时！页面截图已保存为 github_error_screenshot.png")
            raise
