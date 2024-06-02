from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def success_order_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="order-successful-icon"]')

    def id_paragraph(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="order-successful-id"]')

    def return_order_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="order-return-button"]')