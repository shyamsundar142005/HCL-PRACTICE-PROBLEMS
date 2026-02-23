from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
def test_customer_care_valid_query_submission(setup_browser):
    driver = setup_browser
    login(driver)

    driver.find_element(By.LINK_TEXT,"contact").click()
    driver.find_element(By.ID,"name").send_keys("john")
    driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
    driver.find_element(By.ID,"phone").send_keys("9876543210")
    driver.find_element(By.ID,"message").send_keys("SAMPLE MESSAGE")
    driver.find_element(By.XPATH,'//*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input').click()
    wait=WebDriverWait(driver,10)
    title = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="rightPanel"]/p[2]')
        )
    ).text
    assert title == "A Customer Care Representative will be contacting you."

def test_customer_care_name_empty_query_submission(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"contact").click()
    #driver.find_element(By.ID,"name").send_keys("john")
    driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
    driver.find_element(By.ID,"phone").send_keys("9876543210")
    driver.find_element(By.ID,"message").send_keys("SAMPLE MESSAGE")
    driver.find_element(By.XPATH,'//*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input').click()
    wait=WebDriverWait(driver,10)
    title = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"name.errors")
        )
    ).text
    assert title == "Name is required."
    print("✅ Feedback Failed!- Name is required.")
    print("\n")

def test_customer_care_email_empty_query_submission(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"contact").click()
    driver.find_element(By.ID,"name").send_keys("john")
    #driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
    driver.find_element(By.ID,"phone").send_keys("9876543210")
    driver.find_element(By.ID,"message").send_keys("SAMPLE MESSAGE")
    driver.find_element(By.XPATH,'//*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input').click()
    wait=WebDriverWait(driver,10)
    title = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"email.errors")
        )
    ).text
    assert title == "Email is required."
    print("✅ Feedback Failed!-Email is required.")
    print("\n")

def test_customer_care_phonenum_empty_query_submission(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"contact").click()
    driver.find_element(By.ID,"name").send_keys("john")
    driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
    #driver.find_element(By.ID,"phone").send_keys("9876543210")
    driver.find_element(By.ID,"message").send_keys("SAMPLE MESSAGE")
    driver.find_element(By.XPATH,'//*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input').click()
    wait=WebDriverWait(driver,10)
    title = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"phone.errors")
        )
    ).text
    assert title == "Phone is required."
    print("✅ Feedback Failed!- Phone is required.")
    print("\n")
def test_customer_care_msg_empty_query_submission(setup_browser):
    driver = setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"contact").click()
    driver.find_element(By.ID,"name").send_keys("john")
    driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
    driver.find_element(By.ID,"phone").send_keys("9876543210")
    #driver.find_element(By.ID,"message").send_keys("SAMPLE MESSAGE")
    driver.find_element(By.XPATH,'//*[@id="contactForm"]/table/tbody/tr[5]/td[2]/input').click()
    wait=WebDriverWait(driver,10)
    title = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"message.errors")
        )
    ).text
    assert title == "Message is required."
    print("✅ Feedback Failed!- Message required.")
    print("\n")
