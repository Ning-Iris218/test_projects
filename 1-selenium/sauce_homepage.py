from selenium.webdriver.common.by import By

class SauceHomepage:
    _CART_LINK= (By.CLASS_NAME,'shopping_cart_link') #私有常量

    def __init__(self,driver):
        self.driver=driver

    def is_cart_visible(self):
        return self.driver.find_element(*self._CART_LINK).is_displayed()