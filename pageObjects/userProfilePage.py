from selenium.webdriver.common.by import By


class UserProfile:
    def __init__(self, driver):
        self.driver = driver

    def enable_change_username_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="user-profile-change-credentials-username-btn"]')

    def change_username_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="user-profile-new-username-input"]')

    def save_username_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="user-profile-save-credentials-username-btn"]')

    def enable_change_password_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="user-profile-change-credentials-password-btn"]')

    def change_password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="user-profile-new-password-input"]')

    def confirm_password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="user-profile-new-confirm-password-input"]')

    def save_password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="user-profile-save-credentials-password-btn"]')

    def success_box(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="success-box"]')


