from selenium.webdriver.common.by import By


class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def product_title_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="details-title"]')

    def warranty_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="details-waranty"]')

    def return_option_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="details-return-option"]')

    def add_to_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="details-add-to-cart-btn"]')

    def price_paragraph(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="details-price"]')
