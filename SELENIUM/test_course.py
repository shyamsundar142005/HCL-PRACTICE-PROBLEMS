# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import pytest
# @pytest.fixture(scope="function")
# def setup_browser(request):
#     driver=webdriver.Chrome()
#     driver.get("https://parabank.parasoft.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
# def login(driver):
#     driver.find_element(By.NAME, "username").send_keys("john")
#     driver.find_element(By.NAME, "password").send_keys("demo")
#     driver.find_element(By.XPATH, "//input[@value='Log In']").click()
#
# def test_free_trials_req(setup_browser):
#     driver = setup_browser
#     login(driver)
#
#     # Click Products
#     driver.find_element(By.LINK_TEXT, "Products").click()
#
#     # Click Get Started
#     get_started = driver.find_element(By.XPATH, "//a[text()='Get Started']")
#     driver.execute_script("arguments[0].click();", get_started)
#
#     # Click Start Free Trial
#     free_trial = driver.find_element(By.XPATH, "//a[text()='Start Free Trial']")
#     driver.execute_script("arguments[0].click();", free_trial)
#
#     # Email
#     email = driver.find_element(By.XPATH, "//input[@type='email']")
#     email.send_keys("220801200@rajalakshmi.edu.in")
#
#     # First Name (REQUIRED)
#     first_name = driver.find_element(
#         By.XPATH, "//input[contains(@id,'firstname')]"
#     )
#     first_name.send_keys("John")
#
#     # Last Name (REQUIRED)
#     last_name = driver.find_element(
#         By.XPATH, "//input[contains(@id,'lastname')]"
#     )
#     last_name.send_keys("Smith")
#
#     # Job Title
#     job_title = driver.find_element(
#         By.XPATH, "//input[contains(@id,'jobtitle')]"
#     )
#     job_title.send_keys("Testing")
#
#     # Country dropdown
#     country = driver.find_element(
#         By.XPATH, "//select[contains(@id,'country')]"
#     )
#     Select(country).select_by_visible_text("India")
#
#     # Submit button
#     submit_btn = driver.find_element(By.XPATH, "//input[contains(@class,'hs-button')]")
#     driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
#     driver.execute_script("arguments[0].click();", submit_btn)
#
#     # Wait for Thank You message
#     wait = WebDriverWait(driver, 20)
#     text = wait.until(
#         EC.visibility_of_element_located(
#             (By.XPATH, "//h2[contains(text(),'Thank You')]")
#         )
#     ).text
#
#     assert text == "Thank You!"
#     print("✅ Free Trial Submitted Successfully!")
#
#
#
#
#
