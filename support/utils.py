import json

import mysql.connector
import requests

from pageObjects.pageObjectManager import PageObjectManager


def databse_connector():
    mydb = mysql.connector.connect(
        host="localhost",
        database="test-app-dev",
        user="devuser",
        password="12345678"
    )
    return mydb


def delete_order(id):
    mydb = databse_connector()
    mycursor = mydb.cursor()
    query = "DELETE FROM Orders WHERE orderId = '" + id + "'"
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()


def deregister_user(user_name):
    mydb = databse_connector()
    mycursor = mydb.cursor()
    query = "DELETE FROM users WHERE username = '" + user_name + "'"
    mycursor.execute(query)
    mydb.commit()


def accept_cookie(driver):
    driver.add_cookie({
        'name': "Cookie",
        "value": "true"
    })
    driver.refresh()


def login(driver, username, password):
    page_object_manager = PageObjectManager(driver)
    page_object_manager.loginPage.username_input().send_keys(username)
    page_object_manager.loginPage.password_input().send_keys(password)
    page_object_manager.loginPage.login_button().click()
    assert page_object_manager.loginPage.success_box_div().is_displayed()


def quick_login(driver, username, password):
    response = requests.post('http://localhost:3000/api/v1/login', {"username": username, "password": password}).json()

    user_data = {"token": response["token"], "username": response["username"]}
    script = f'window.localStorage.setItem("User", `{json.dumps(user_data)}`);'
    driver.execute_script(script)
    driver.refresh()