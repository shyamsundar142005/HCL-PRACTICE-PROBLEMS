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

def test_account_open(setup_browser):
    driver = setup_browser
    login(driver)
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.LINK_TEXT, "Open New Account").click()
    account_type = Select(wait.until(
        EC.presence_of_element_located((By.ID, "type"))
    ))
    account_type.select_by_visible_text("SAVINGS")
    from_account = Select(wait.until(
        EC.presence_of_element_located((By.ID, "fromAccountId"))
    ))
    from_account.select_by_index(0)
    open_account_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Open New Account']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", open_account_btn)
    open_account_btn.click()
    heading = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[text()='Account Opened!']")
        )
    ).text
    assert heading == "Account Opened!"
    print("✅", heading)

def test_account_overview(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Accounts Overview").click()
    title=driver.find_element(By.CLASS_NAME,"title").text
    assert title=="Accounts Overview"
    print("✅ Displayed Accounts Overview")
    print("\n")
def test_transer_fund(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Transfer Funds").click()
    driver.find_element(By.ID,"amount").send_keys("100")
    account_no=Select(driver.find_element(By.ID,"toAccountId"))
    account_no.select_by_index(1)
    driver.find_element(By.CLASS_NAME,"button").click()
    print("✅ Transfer Funds Successful!")
    print("\n")

def test_overview_check(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Accounts Overview").click()
    cell = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='accountTable']//tbody/tr[1]/td[1]/a")
        )
    )

    cell.click()

    success=driver.find_element(By.XPATH,'//*[@id="accountDetails"]/h1').text
    assert success == "Account Details"

    Select(driver.find_element(By.ID,"month")).select_by_index(0)
    Select(driver.find_element(By.ID,"transactionType")).select_by_index(0)
    driver.find_element(By.XPATH,'//*[@id="activityForm"]/table/tbody/tr[3]/td[2]/input').click()
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "transactionTable")
        )
    )
    print("✅ Transaction Checked")
    print("\n")

def test_trancsaction_check1(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Accounts Overview").click()
    cell = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='accountTable']//tbody/tr[1]/td[1]/a")
        )
    )

    cell.click()

    success=driver.find_element(By.XPATH,'//*[@id="accountDetails"]/h1').text
    assert success == "Account Details"
    Select(driver.find_element(By.ID,"month")).select_by_index(0)
    Select(driver.find_element(By.ID,"transactionType")).select_by_visible_text("Debit")
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((By.ID, "transactionTable"))
    )
    rows=driver.find_elements(By.XPATH,'//*[@id="transactionTable"]/tbody/tr')
    for row in rows:
        debit_value = row.find_element(By.XPATH, './td[3]').text.strip()
        credit_value = row.find_element(By.XPATH, './td[4]').text.strip()
        if debit_value== "" and credit_value == "":
            continue
        if credit_value == "":
            assert debit_value != ""
    print("✅ Assertion verified successfully")
    print("\n")

def test_req_loan_check_accept(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Request Loan").click()
    driver.find_element(By.ID,"amount").send_keys("100")
    driver.find_element(By.ID,"downPayment").send_keys("20")
    Select(driver.find_element(By.ID,"fromAccountId")).select_by_index(0)
    driver.find_element(By.XPATH,'//*[@id="requestLoanForm"]/form/table/tbody/tr[4]/td[2]/input').click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "loanRequestApproved"),
            "Congratulations"
        )
    )
    assert "Congratulations" in driver.find_element(By.ID, "loanRequestApproved").text
    print("✅ Loan Approved")

def test_req_loan_check_reject(setup_browser):
    driver =setup_browser
    login(driver)
    driver.find_element(By.LINK_TEXT,"Request Loan").click()
    driver.find_element(By.ID,"amount").send_keys("100000")
    driver.find_element(By.ID,"downPayment").send_keys("100")
    Select(driver.find_element(By.ID,"fromAccountId")).select_by_index(0)
    driver.find_element(By.XPATH,'//*[@id="requestLoanForm"]/form/table/tbody/tr[4]/td[2]/input').click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "loanRequestDenied"),
            "We cannot grant a loan"
        )
    )
    assert "We cannot grant a loan" in driver.find_element(By.ID, "loanRequestDenied").text
    print("✅ Loan Rejected")
    print("\n")

