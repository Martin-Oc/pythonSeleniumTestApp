from selenium.webdriver.common.by import By


class MyOrdersPage:
    def __init__(self, driver):
        self.driver = driver

    def my_orders_entry_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="header-item-my-orders"]')

    def record_paragraph(self, id):
        return self.driver.find_element(By.XPATH, '//p[contains(text(),"' + str(id) + '")]/..')

