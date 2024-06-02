from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def username_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="username-input"]')

    def password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="password-input"]')

    def password_confirmation_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="password-confirmation-input"]')

    def email_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="email-input"]')

    def name_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="name-input"]')

    def address_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="address-input"]')

    def country_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="country-input"]')

    def city_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="city-input"]')

    def postcode_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="post-code-input"]')

    def phone_number_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="phone-number-input"]')

    def terms_and_condition_input(self):
        return self.driver.find_element(By.XPATH, '(//label[@class="switch"])[2]')

    def business_account_input(self):
        return self.driver.find_element(By.XPATH, '(//label[@class="switch"])[3]')

    def company_reg_number_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="company-registration-number-input"]')

    def vat_no_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="VAT-input"]')

    def bic_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="BIC-input"]')

    def iban_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="IBAN-input"]')

    def account_holder_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="name-of-bank-account-input"]')

    def register_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="save-values-btn"]')

    def success_box_div(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="success-box"]')
