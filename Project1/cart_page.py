from selenium.webdriver.common.by import By

class Cart_Page:
    _REMOVE_BACKPACK=(By.ID,'remove-sauce-labs-backpack')
    _CHECK_OUT=(By.ID,'checkout')

    def __init__(self,driver):
        self.driver = driver

    def remove_backpack(self):
        self.driver.find_element(*self._REMOVE_BACKPACK).click()

    def checkout(self):
        self.driver.find_element(*self._CHECK_OUT).click()

    def get_items_count(self):
        items=self.driver.find_elements(By.CLASS_NAME,'cart_item')
        return len(items)