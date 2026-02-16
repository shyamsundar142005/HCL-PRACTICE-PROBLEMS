from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="function")
def setup_browser():
    driver =webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def login(driver):
    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()

def test_billpay_success(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Bill Pay").click()
    driver.find_element(By.NAME, "payee.name").send_keys("John")
    driver.find_element(By.NAME, "payee.address.street").send_keys("kanchipuram")
    driver.find_element(By.NAME, "payee.address.city").send_keys("Kansa")
    driver.find_element(By.NAME, "payee.address.state").send_keys("TN")
    driver.find_element(By.NAME, "payee.address.zipCode").send_keys("123456")
    driver.find_element(By.NAME, "payee.phoneNumber").send_keys("9876543210")
    driver.find_element(By.NAME, "payee.accountNumber").send_keys("12345")
    driver.find_element(By.NAME, "verifyAccount").send_keys("12345")
    driver.find_element(By.NAME, "amount").send_keys("100")
    Select(driver.find_element(By.NAME,"fromAccountId")).select_by_index(1)
    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()

    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Bill Payment Complete']"))
    ).text

    assert success == "Bill Payment Complete"
    print("✅",success)
    print("\n")

def test_billpay_error_missing_name(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Bill Pay").click()
   # driver.find_element(By.NAME, "payee.name").send_keys("")
    driver.find_element(By.NAME, "payee.address.street").send_keys("kanchipuram")
    driver.find_element(By.NAME, "payee.address.city").send_keys("Kansa")
    driver.find_element(By.NAME, "payee.address.state").send_keys("TN")
    driver.find_element(By.NAME, "payee.address.zipCode").send_keys("123456")
    driver.find_element(By.NAME, "payee.phoneNumber").send_keys("9876543210")
    driver.find_element(By.NAME, "payee.accountNumber").send_keys("12345")
    driver.find_element(By.NAME, "verifyAccount").send_keys("12345")
    driver.find_element(By.NAME, "amount").send_keys("100")
    Select(driver.find_element(By.NAME,"fromAccountId")).select_by_index(1)
    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "validationModel-name"))
    ).text
    assert success == "Payee name is required."
    print("✅ Bill payment failed: Payee name is required.")

def test_billpay_error_missing_address(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Bill Pay").click()
    driver.find_element(By.NAME, "payee.name").send_keys("shyam")
    #driver.find_element(By.NAME, "payee.address.street").send_keys("kanchipuram")
    driver.find_element(By.NAME, "payee.address.city").send_keys("Kansa")
    driver.find_element(By.NAME, "payee.address.state").send_keys("TN")
    driver.find_element(By.NAME, "payee.address.zipCode").send_keys("123456")
    driver.find_element(By.NAME, "payee.phoneNumber").send_keys("9876543210")
    driver.find_element(By.NAME, "payee.accountNumber").send_keys("12345")
    driver.find_element(By.NAME, "verifyAccount").send_keys("12345")
    driver.find_element(By.NAME, "amount").send_keys("100")
    Select(driver.find_element(By.NAME,"fromAccountId")).select_by_index(1)
    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "validationModel-address"))
    ).text
    assert success == "Address is required."
    print("✅ Bill payment failed: Address field is required.")
    print("\n")

def test_billpay_error_missing_city(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Bill Pay").click()
    driver.find_element(By.NAME, "payee.name").send_keys("shyam")
    driver.find_element(By.NAME, "payee.address.street").send_keys("kanchipuram")
    #driver.find_element(By.NAME, "payee.address.city").send_keys("Kansa")
    driver.find_element(By.NAME, "payee.address.state").send_keys("TN")
    driver.find_element(By.NAME, "payee.address.zipCode").send_keys("123456")
    driver.find_element(By.NAME, "payee.phoneNumber").send_keys("9876543210")
    driver.find_element(By.NAME, "payee.accountNumber").send_keys("12345")
    driver.find_element(By.NAME, "verifyAccount").send_keys("12345")
    driver.find_element(By.NAME, "amount").send_keys("100")
    Select(driver.find_element(By.NAME,"fromAccountId")).select_by_index(1)
    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "validationModel-city"))
    ).text
    assert success == "City is required."
    print("✅ Bill payment failed: City field is required.")
    print("\n")
def test_billpay_error_missing_state(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Bill Pay").click()
    driver.find_element(By.NAME, "payee.name").send_keys("shyam")
    driver.find_element(By.NAME, "payee.address.street").send_keys("kanchipuram")
    driver.find_element(By.NAME, "payee.address.city").send_keys("Kansa")
    #driver.find_element(By.NAME, "payee.address.state").send_keys("TN")
    driver.find_element(By.NAME, "payee.address.zipCode").send_keys("123456")
    driver.find_element(By.NAME, "payee.phoneNumber").send_keys("9876543210")
    driver.find_element(By.NAME, "payee.accountNumber").send_keys("12345")
    driver.find_element(By.NAME, "verifyAccount").send_keys("12345")
    driver.find_element(By.NAME, "amount").send_keys("100")
    Select(driver.find_element(By.NAME,"fromAccountId")).select_by_index(1)
    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "validationModel-state"))
    ).text
    assert success == "State is required."
    print("✅ Bill payment failed: State field is required.")
    print("\n")

def test_billpay_error_account_mismatch(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Bill Pay").click()
    driver.find_element(By.NAME, "payee.name").send_keys("shyam")
    driver.find_element(By.NAME, "payee.address.street").send_keys("kanchipuram")
    driver.find_element(By.NAME, "payee.address.city").send_keys("Kansa")
    driver.find_element(By.NAME, "payee.address.state").send_keys("TN")
    driver.find_element(By.NAME, "payee.address.zipCode").send_keys("123456")
    driver.find_element(By.NAME, "payee.phoneNumber").send_keys("9876543210")
    driver.find_element(By.NAME, "payee.accountNumber").send_keys("12345")
    driver.find_element(By.NAME, "verifyAccount").send_keys("1234")
    driver.find_element(By.NAME, "amount").send_keys("100")
    Select(driver.find_element(By.NAME,"fromAccountId")).select_by_index(1)
    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "validationModel-verifyAccount-mismatch"))
    ).text
    assert success == "The account numbers do not match."
    print("✅ Bill payment failed: Account number and verification do not match.")
    print("\n")

