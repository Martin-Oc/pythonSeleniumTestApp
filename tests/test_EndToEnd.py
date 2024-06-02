import pickle
import re
import time

import pytest
from pageObjects.pageObjectManager import PageObjectManager
from selenium.webdriver.support.ui import Select

from support.utils import delete_order, accept_cookie, login, quick_login


@pytest.mark.usefixtures("create_users")
class TestEndToEnd:
    def test_submit_order_no_logged_in_user(self, setup):
        page_object_manager = PageObjectManager(setup)
        assert (page_object_manager.homePage.cookie_banner().is_displayed())
        page_object_manager.homePage.cookie_banner_allow_button().click()
        try:
            assert (page_object_manager.homePage.cookie_banner() == False)
        except:
            print('No element present')
        page_object_manager.homePage.filter_input().send_keys('T')
        page_object_manager.homePage.filter_clothing_button().click()
        assert len(page_object_manager.homePage.items_div()) == 1
        page_object_manager.homePage.add_to_cart_button()[0].click()
        page_object_manager.homePage.modal_navigate_to_cart_button().click()
        # cart page
        assert len(page_object_manager.cartPage.cart_items()) == 1
        assert "15.99 €" in page_object_manager.cartPage.cart_items()[0].text
        assert "T-Shirt" in page_object_manager.cartPage.cart_items()[0].text
        total_price = page_object_manager.cartPage.total_price().text
        page_object_manager.cartPage.shipping_button().click()
        # shipping page
        page_object_manager.shippingPage.personal_pickip_option().click()
        page_object_manager.shippingPage.credit_cart_option().click()
        page_object_manager.shippingPage.address_button().click()
        # address page
        page_object_manager.addressPage.email_input().send_keys("testMail@test.sk")
        page_object_manager.addressPage.name_input().send_keys('Janko Mrkvicka')
        page_object_manager.addressPage.address_input().send_keys('Hlavna 258')
        Select(page_object_manager.addressPage.country_input()).select_by_value("Slovakia")
        page_object_manager.addressPage.city_input().send_keys("Bratislava")
        page_object_manager.addressPage.postcode_input().send_keys('987 58')
        page_object_manager.addressPage.phone_input().send_keys("+421 987 654 321")
        page_object_manager.addressPage.option_checkboxes()[1].click()
        page_object_manager.addressPage.summary_button().click()
        # summary page
        assert (page_object_manager.summaryPage.full_name_label().text == "Janko Mrkvicka")
        assert (page_object_manager.summaryPage.email_label().text == "testMail@test.sk")
        assert (page_object_manager.summaryPage.address_label().text == "Hlavna 258")
        assert (page_object_manager.summaryPage.country_label().text == "Slovakia")
        assert (page_object_manager.summaryPage.city_label().text == "Bratislava")
        assert (page_object_manager.summaryPage.postcode_label().text == "987 58")
        assert (page_object_manager.summaryPage.phone_number_label().text == "+421 987 654 321")
        assert (page_object_manager.summaryPage.delivery_method_label().text == "Personal pickup")
        assert (page_object_manager.summaryPage.payment_type_label().text == "Credit / Debit Card")
        assert (page_object_manager.summaryPage.total_price().text == total_price)
        page_object_manager.summaryPage.order_button().click()
        # successful order
        assert page_object_manager.orderPage.success_order_icon().is_displayed()
        order_id = re.findall(r'\d+', page_object_manager.orderPage.id_paragraph().text)
        print(order_id[0])
        page_object_manager.orderPage.return_order_button().click()
        assert page_object_manager.homePage.items_div()[0].is_displayed()
        delete_order(order_id[0])

    def test_submit_order_logged_in_user(self, setup):
        page_object_manager = PageObjectManager(setup)
        assert (page_object_manager.homePage.cookie_banner().is_displayed())
        page_object_manager.homePage.cookie_details_button().click()
        page_object_manager.homePage.cookie_preferencies_input().click()
        page_object_manager.homePage.cookie_stats_input().click()
        page_object_manager.homePage.cookie_banner_allow_button().click()
        # assert cookiebanner confirmed
        cookie = setup.get_cookie("Cookie")
        assert "preferencies%22%3Afalse" in cookie['value']
        assert "stats%22%3Afalse" in cookie['value']
        # login
        page_object_manager.loginPage.login_entry_button().click()
        login(setup, 'test_user', '12345678')
        # home page
        page_object_manager.homePage.shop_entry_button().click()
        page_object_manager.homePage.items_div()[2].click()
        # product detail page
        assert page_object_manager.productDetailPage.product_title_heading().text == "Backpack"
        productPrice = page_object_manager.productDetailPage.price_paragraph().text
        page_object_manager.productDetailPage.warranty_checkbox().click()
        page_object_manager.productDetailPage.return_option_checkbox().click()
        page_object_manager.productDetailPage.add_to_cart_button().click()
        page_object_manager.homePage.modal_navigate_to_cart_button().click()
        # cart page
        assert len(page_object_manager.cartPage.cart_items()) == 1
        assert "79.99 €" in page_object_manager.cartPage.cart_items()[0].text
        assert "Backpack" in page_object_manager.cartPage.cart_items()[0].text
        total_price = page_object_manager.cartPage.total_price().text
        page_object_manager.cartPage.shipping_button().click()
        # shipping page
        page_object_manager.shippingPage.personal_pickip_option().click()
        page_object_manager.shippingPage.credit_cart_option().click()
        page_object_manager.shippingPage.address_button().click()
        # address page
        page_object_manager.addressPage.summary_button().click()
        # summary page
        assert (page_object_manager.summaryPage.total_price().text == total_price)
        page_object_manager.summaryPage.order_button().click()
        # successful order
        assert page_object_manager.orderPage.success_order_icon().is_displayed()
        order_id = re.findall(r'\d+', page_object_manager.orderPage.id_paragraph().text)
        print(order_id[0])
        page_object_manager.orderPage.return_order_button().click()
        assert page_object_manager.homePage.items_div()[0].is_displayed()
        # my orders page
        page_object_manager.myOrdersPage.my_orders_entry_button().click()
        assert page_object_manager.myOrdersPage.record_paragraph(order_id[0]).is_displayed()
        assert total_price in page_object_manager.myOrdersPage.record_paragraph(order_id[0]).text
        delete_order(order_id[0])

@pytest.mark.usefixtures("create_users")
class TestAuthorisation:
    def test_login_and_logout(self, setup):
        page_object_manager = PageObjectManager(setup)
        # cookie
        accept_cookie(setup)
        # login
        page_object_manager.loginPage.login_entry_button().click()
        login(setup, 'test_user', '12345678')
        # navigate to login
        setup.get('http://localhost:3000/logIn')
        try:
            assert not (page_object_manager.loginPage.username_input() == True)
        except:
            print('No element present')
        # logout
        page_object_manager.loginPage.logout_button().click()
        setup.get('http://localhost:3000/logIn')
        assert page_object_manager.loginPage.username_input().is_displayed()
        assert page_object_manager.loginPage.login_entry_button().is_displayed()

    def test_registration(self, setup):
        page_object_manager = PageObjectManager(setup)
        # cookie
        accept_cookie(setup)
        # login page
        page_object_manager.loginPage.login_entry_button().click()
        page_object_manager.loginPage.registration_button().click()
        # registration page
        page_object_manager.registrationPage.username_input().send_keys('test_registered')
        page_object_manager.registrationPage.password_input().send_keys('12345678')
        page_object_manager.registrationPage.password_confirmation_input().send_keys('12345678')
        page_object_manager.registrationPage.email_input().send_keys('test_registered@test.ks')
        page_object_manager.registrationPage.name_input().send_keys('Janko Test')
        page_object_manager.registrationPage.address_input().send_keys("Bocna 85")
        Select(page_object_manager.registrationPage.country_input()).select_by_value("Slovakia")
        page_object_manager.registrationPage.city_input().send_keys('Kosice')
        page_object_manager.registrationPage.postcode_input().send_keys('98 564')
        page_object_manager.registrationPage.phone_number_input().send_keys('+421 687 879 654')
        page_object_manager.registrationPage.terms_and_condition_input().click()
        page_object_manager.registrationPage.register_button().click()
        assert page_object_manager.registrationPage.success_box_div().is_displayed()

    def test_registration_business_account(self, setup):
        page_object_manager = PageObjectManager(setup)
        # cookie
        accept_cookie(setup)
        # login page
        page_object_manager.loginPage.login_entry_button().click()
        page_object_manager.loginPage.registration_button().click()
        # registration page
        page_object_manager.registrationPage.username_input().send_keys('test_registered_business')
        page_object_manager.registrationPage.password_input().send_keys('12345678')
        page_object_manager.registrationPage.password_confirmation_input().send_keys('12345678')
        page_object_manager.registrationPage.email_input().send_keys('test_registered@test.ks')
        page_object_manager.registrationPage.name_input().send_keys('Janko Test')
        page_object_manager.registrationPage.address_input().send_keys("Bocna 85")
        Select(page_object_manager.registrationPage.country_input()).select_by_value("Slovakia")
        page_object_manager.registrationPage.city_input().send_keys('Kosice')
        page_object_manager.registrationPage.postcode_input().send_keys('98 564')
        page_object_manager.registrationPage.phone_number_input().send_keys('+421 687 879 654')
        page_object_manager.registrationPage.terms_and_condition_input().click()
        page_object_manager.registrationPage.business_account_input().click()
        page_object_manager.registrationPage.company_reg_number_input().send_keys('6868462')
        page_object_manager.registrationPage.vat_no_input().send_keys('66468879')
        page_object_manager.registrationPage.bic_input().send_keys('AD468494')
        page_object_manager.registrationPage.iban_input().send_keys('SK846468461646516')
        page_object_manager.registrationPage.account_holder_input().send_keys('Janko Petko')
        page_object_manager.registrationPage.register_button().click()
        assert page_object_manager.registrationPage.success_box_div().is_displayed()


@pytest.mark.usefixtures("create_users")
class TestUserProfile:
    def test_change_username_and_password(self, setup):
        page_object_manager = PageObjectManager(setup)
        # basic log in and cookie accept
        accept_cookie(setup)
        quick_login(setup, "test_user", "12345678")
        # navigate to user profile
        setup.get("http://localhost:3000/user-profile")
        # change username
        page_object_manager.userProfilePage.enable_change_username_button().click()
        page_object_manager.userProfilePage.change_username_input().send_keys("test_user2")
        page_object_manager.userProfilePage.save_username_input().click()
        assert page_object_manager.userProfilePage.success_box().is_displayed()
        # change password
        page_object_manager.userProfilePage.enable_change_password_button().click()
        page_object_manager.userProfilePage.change_password_input().send_keys("123456789")
        page_object_manager.userProfilePage.confirm_password_input().send_keys("123456789")
        page_object_manager.userProfilePage.save_password_input().click()
        assert page_object_manager.userProfilePage.success_box().is_displayed()
        # logout and log in
        page_object_manager.loginPage.logout_button().click()
        setup.get("http://localhost:3000/logIn")
        login(setup, 'test_user2', '123456789')
        assert page_object_manager.loginPage.success_box_div().is_displayed()