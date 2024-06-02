from selenium.webdriver.common.by import By


class SummaryPage:
    def __init__(self,driver):
        self.driver = driver

    def full_name_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-name-DataLabel"]')

    def email_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-email-DataLabel"]')

    def address_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-address-DataLabel"]')

    def country_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-country-DataLabel"]')

    def city_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-city-DataLabel"]')

    def postcode_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-post-code-DataLabel"]')

    def phone_number_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-phone-number-DataLabel"]')

    def delivery_method_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-delivery-method-DataLabel"]')

    def payment_type_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-payment-type-DataLabel"]')

    def product_divs(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type*="summary-single-item-"]')

    def total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-total-price-price"]')

    def order_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="summary-order"]')