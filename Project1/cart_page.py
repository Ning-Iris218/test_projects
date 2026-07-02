from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_Page:
    _REMOVE_BACKPACK=(By.ID,'remove-sauce-labs-backpack')
    _CHECK_OUT=(By.ID,'checkout')

    def __init__(self,driver):
        self.driver = driver

    def remove_backpack(self):
        self.driver.find_element(*self._REMOVE_BACKPACK).click()

    def checkout(self):
        print(f"准备点击结算，当前网址是: {self.driver.current_url}")
        print(f"当前页面的标题是: {self.driver.title}")
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._CHECK_OUT)
        )
        self.driver.execute_script("arguments[0].click();", checkout_btn)


    def get_items_count(self):
        items=self.driver.find_elements(By.CLASS_NAME,'cart_item')
        return len(items)