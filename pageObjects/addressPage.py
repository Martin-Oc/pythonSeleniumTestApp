from selenium.webdriver.common.by import By


class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    def email_input(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="email-input"]')

    def name_input(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="name-input"]')

    def address_input(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="address-input"]')

    def country_input(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="country-input"]')

    def city_input(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="city-input"]')

    def postcode_input(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="post-code-input"]')

    def phone_input(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="phone-number-input"]')

    def option_checkboxes(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'label.switch')

    def summary_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="save-values-btn"]')
