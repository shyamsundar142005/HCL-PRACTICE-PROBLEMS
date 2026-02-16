from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="function")
def setup_browser():
    driver =webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def login(driver):
    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()

def test_solution_btn_failure(setup_browser):
    driver = setup_browser
    login(driver)
    wait = WebDriverWait(driver, 10)
    text=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"Solutions"))).text
    assert text == "Solutions"
    driver.save_screenshot("image.png")
    print("❌ URL is not working")
    print("\n")

def test_about_btn_status(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT, "About Us").click()
    wait = WebDriverWait(driver, 10)
    title=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="rightPanel"]/h1'))).text
    assert title == "ParaSoft Demo Website"
    print("✅ About Button Status Success")
    print("\n")

def test_service_btn_status(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT, "Services").click()
    wait = WebDriverWait(driver, 10)
    title=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"heading"))).text
    assert title == "Available Bookstore SOAP services:"
    print("✅ Service Button Status Success")
    print("\n")

def test_Products_btn_status(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT, "Products").click()
    wait = WebDriverWait(driver, 10)
    title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
".mb-\\[16rem\\].border-b-\\[4px\\].border-blue300.inline-block.uppercase.font-bold.text-\\[16rem\\].pb-\\[8rem\\].font-zeitung"))
    ).text
    assert title == "PRODUCTS"

    print("✅ Products Button Status Success")
    print("\n")

def test_location_btn_status(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT, "Locations").click()
    wait = WebDriverWait(driver, 10)
    title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                         ".mb-\\[16rem\\].border-b-\\[4px\\].border-blue300.inline-block.uppercase.font-bold.text-\\[16rem\\].pb-\\[8rem\\].font-zeitung"
                                                         ))).text
    assert title == "SOLUTIONS"

    print("❌ Location Button Status Failed")
    print("\n")

def test_admin_btn_status(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT, "Admin Page").click()
    wait = WebDriverWait(driver, 10)
    title=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="rightPanel"]/h1'))).text
    assert title == "Administration"
    print("✅ Admin Button Status Success")
    print("\n")



