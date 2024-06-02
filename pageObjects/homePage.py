from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def shop_entry_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="header-item-shop"]')

    def cookie_banner(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="cookie-banner"]')

    def cookie_details_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="cookie-banner-header-details-btn"]')

    def cookie_preferencies_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="cookie-banner-preferencies-span"]')

    def cookie_stats_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="cookie-banner-stats-span"]')

    def cookie_banner_allow_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="cookie-banner-allow-btn"]')

    def filter_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="filter-search-input"]')

    def filter_clothing_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[data-type="filter-category-button-Clothing"]')

    def items_div(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '[data-type*="single-product-"]')

    def add_to_cart_button(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '[data-type*="product-cart-button-"]')

    def modal_navigate_to_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-type="navigate-to-cart"]')