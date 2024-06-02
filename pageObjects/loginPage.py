from selenium.webdriver.common.by import By


class LogInPage():
    def __init__(self, driver):
        self.driver = driver

    def login_entry_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="header-item-logIn"]')

    def logout_entry_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'data-type="header-log-out"]')

    def username_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="username-Input"]')

    def password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="password-Input"]')

    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="log-in-button"]')

    def success_box_div(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="success-box"]')

    def logout_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="header-log-out"]')

    def registration_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="registration-button"]')
