import pytest
from selenium import webdriver
from support.utils import databse_connector, deregister_user


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/shop')
    driver.implicitly_wait(5)
    yield driver


@pytest.fixture(scope="class")
def create_users():
    mydb = databse_connector()
    mycursor = mydb.cursor()
    query = """INSERT INTO users (
        username, password, email, name, address, city, post_code, phone_number, country,
        newsletter, terms_and_condition, bussiness_account, compaty_reg_number, BIC, VAT, IBAN, bank_account_holder
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    value = (
        'test_user', '12345678', 'johnSmilga@test.com', 'John Smilga', 'Main 32', 'Bratislava', '14 759', '0258471698',
        'Slovakia', 'true', 'true', 'false', '', '', '', '', ''
    )
    mycursor.execute(query, value)
    mydb.commit()

    yield
    deregister_user("test_user")
    deregister_user("test_registered")
    deregister_user("test_registered_business")
    deregister_user("test_user2")

    mycursor.close()
    mydb.close()