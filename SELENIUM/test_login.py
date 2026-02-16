from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import random
import string

def generate_unique_value():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

username=generate_unique_value()

@pytest.fixture(scope="function")
def setup_browser():
    driver =webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_register(setup_browser):
    driver = setup_browser
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "customer.firstName").send_keys("shyam")
    driver.find_element(By.ID,"customer.lastName").send_keys("sundar")
    driver.find_element(By.ID,"customer.address.street").send_keys("kanchipuram")
    driver.find_element(By.ID,"customer.address.city").send_keys("kanchipuram")
    driver.find_element(By.ID,"customer.address.state").send_keys("tamilnadu")
    driver.find_element(By.ID,"customer.address.zipCode").send_keys("12345")
    driver.find_element(By.ID,"customer.phoneNumber").send_keys("9876543210")
    driver.find_element(By.ID,"customer.ssn").send_keys("123")
    driver.find_element(By.ID,"customer.username").send_keys(username)
    driver.find_element(By.ID,"customer.password").send_keys("test@123")
    driver.find_element(By.ID,"repeatedPassword").send_keys("test@123")
    driver.find_element(By.XPATH, "//input[@value='Register']").click()
    success_msg = driver.find_element(By.XPATH, "//p[contains(text(),'Your account was created successfully')]").text
    assert "Your account was created successfully. You are now logged in." in success_msg
    print("✅ Registration Successful!")
    print("\n")
def test_validlogin(setup_browser):
    driver = setup_browser
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("john")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("demo")
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    heading = driver.find_element(By.XPATH, "//*[@id='showOverview']/h1").text
    assert heading == "Accounts Overview"
    print("✅ Login Successful!")
    print("\n")

def test_blankusername(setup_browser):
    driver = setup_browser
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123")
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    heading=driver.find_element(By.XPATH, "//*[@id='rightPanel']/p").text
    assert heading == "Please enter a username and password."
    print("✅ Login Failed!- Username Required")
    print("\n")

def test_blank_password(setup_browser):
    driver = setup_browser
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("shyam")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    heading=driver.find_element(By.XPATH, "//*[@id='rightPanel']/p").text
    assert heading == "Please enter a username and password."
    print("✅ Login Failed!- Password Required")
    print("\n")


def test_invalid_login(setup_browser):
    driver=setup_browser
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("shyamsundar")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123")
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    heading = driver.find_element(By.XPATH, '//*[@id="rightPanel"]/p').text
    assert heading == "The username and password could not be verified."

    print("✅ Invalid Login Rejected..")
    print("\n")

def login(driver):
        driver.find_element(By.NAME, "username").send_keys("john")
        driver.find_element(By.NAME, "password").send_keys("demo")
        driver.find_element(By.XPATH, "//input[@value='Log In']").click()

def test_logout(setup_browser):
    driver=setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Log Out").click()

    title=driver.find_element(By.XPATH,'//*[@id="leftPanel"]/h2').text
    assert title == "Customer Login"
    print("✅ Log Out Successful!")
    print("\n")

