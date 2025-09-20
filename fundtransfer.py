# parabank_login_simple.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# ---- Config ----
CHROMEDRIVER_PATH = "chromedriver.exe"   # update to the full path if not in the script folder
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
USERNAME = "test1"
PASSWORD = "Th15!s4T3st"
WAIT_SECONDS = 10
transfer_amounts = [10, 100, 1000, 10000]

# ---- Setup WebDriver ----
service = Service(executable_path=CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")  # uncomment to run without opening a browser
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, WAIT_SECONDS)

try:
    print("[INFO] Opening Parabank...")
    driver.get(BASE_URL)

    print("[INFO] Waiting for username field...")
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.clear()
    username_input.send_keys(USERNAME)

    print("[INFO] Entering password...")
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    print("[INFO] Waiting for login confirmation...")
    # Wait for either "Accounts Overview" header or a "Log Out" link as success indicators
    wait.until(EC.any_of(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Accounts Overview')]")),
        EC.presence_of_element_located((By.LINK_TEXT, "Log Out"))
    ))

    print("✅ Login successful!")
    transfer_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds")))

    # Use ActionChains to simulate a mouse click
    actions = ActionChains(driver)
    actions.move_to_element(transfer_link).click().perform()

    

# ---- Perform Transfers ----
    for amount in transfer_amounts:
        print(f"[INFO] Initiating transfer with amount: {amount}")

        # Wait for input field
        amount_field = wait.until(EC.presence_of_element_located((By.ID, "amount")))
        amount_field.clear()
        amount_field.send_keys(str(amount))

        # Click Transfer button
        transfer_btn = driver.find_element(By.CSS_SELECTOR, "input.button[value='Transfer']")
        time.sleep(2)
        transfer_btn.click()

        print(f"💰 Transfer of {amount} submitted!")

        # wait for confirmation page or message
        time.sleep(2)

        # Go back to Transfer Funds page for next test
        transfer_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds")))
        ActionChains(driver).move_to_element(transfer_link).click().perform()

    print("✅ All transfers completed!")

    time.sleep(3)  

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    driver.quit()