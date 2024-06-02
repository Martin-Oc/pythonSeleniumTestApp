from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def cart_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'div[data-type*="cart-single-item-"]')

    def total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="cart-total-price-price"]')

    def shipping_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="cart-billing-navigation"]')