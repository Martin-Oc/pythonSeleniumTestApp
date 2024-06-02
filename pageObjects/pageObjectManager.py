from pageObjects.addressPage import AddressPage
from pageObjects.cartPage import CartPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LogInPage
from pageObjects.myOrdersPage import MyOrdersPage
from pageObjects.orderPage import OrderPage
from pageObjects.productDetailPage import ProductDetailPage
from pageObjects.registrationPage import RegistrationPage
from pageObjects.shippingPage import ShippingPage
from pageObjects.summaryPage import SummaryPage
from pageObjects.userProfilePage import UserProfile


class PageObjectManager:

    def __init__(self, driver):
        self.driver = driver
        self.homePage = HomePage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.shippingPage = ShippingPage(self.driver)
        self.addressPage = AddressPage(self.driver)
        self.summaryPage = SummaryPage(self.driver)
        self.orderPage = OrderPage(self.driver)
        self.loginPage = LogInPage(self.driver)
        self.productDetailPage = ProductDetailPage(self.driver)
        self.myOrdersPage = MyOrdersPage(self.driver)
        self.registrationPage = RegistrationPage(self.driver)
        self.userProfilePage = UserProfile(self.driver)