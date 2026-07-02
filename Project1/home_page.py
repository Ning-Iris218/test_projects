from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    _ADD_BACKPACK=(By.ID,'add-to-cart-sauce-labs-backpack')
    _ALL_ADD=(By.XPATH,"//button[text()='Add to cart']")
    _CART_BUTTON=(By.CLASS_NAME,'shopping_cart_link')


    def __init__(self,driver):
        self.driver=driver

    def add_backpack(self):
        self.driver.find_element(*self._ADD_BACKPACK).click()

    def add_all(self):
        buttons=self.driver.find_elements(*self._ALL_ADD)
        for button in buttons:
            button.click()

    def go_to_cart(self):
        cart_btn=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((self._CART_BUTTON))
        )
        self.driver.execute_script('arguments[0].click();', cart_btn)

        WebDriverWait(self.driver,10).until(EC.url_contains('cart.html'))

