from selenium.webdriver.common.by import By


class ShippingPage:
    def __init__(self,driver):
        self.driver = driver

    def personal_pickip_option(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="shippig-personal-pick-up-input"]')

    def credit_cart_option(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="shippig-card-input"]')

    def address_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="shipping-address-navigation"]')