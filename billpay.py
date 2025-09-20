# parabank_bulk_payments.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# ---- Config ----
CHROMEDRIVER_PATH = "chromedriver.exe"
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
USERNAME = "test"
PASSWORD = "test"
WAIT_SECONDS = 10
NUM_PAYMENTS = 5   # how many bulk payments to simulate

first_names = ["John", "Emma", "Michael", "Sophia", "David", "Olivia", "James", "Ava"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
address = ["Willowbrook", "Stonehaven", "Greenfield", "Oakridge", "Silvermere", "Thornbury", "Rivermist"]
city = ["Eastbridge", "Silverpoint", "Grandchester", "Ironvale", "Brookhaven", "Ashwick", "Rivergate"]
state = ["Silvermont", "Westoria", "Ashlandia", "Crestwood"]
zip_code = [3100, 2300, 3400, 4555, 6000, 5560, 3245]
phone_number = [33232145100, 23546456400, 34745745700, 4557678678675, 609679769600, 5566796796790, 3267967969645]
account_number = 2131231231
amounts = [3100, 2300, 3400, 4555, 6000, 5560, 3245, 8987, 32 , 342 , 34234, 34, 3241, 34161, 6774, 1212]

# ---- Setup WebDriver ----
service = Service(executable_path=CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, WAIT_SECONDS)

try:
    print("[INFO] Opening Parabank...")
    driver.get(BASE_URL)

    # --- Login ---
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.clear()
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    wait.until(EC.any_of(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Accounts Overview')]")),
        EC.presence_of_element_located((By.LINK_TEXT, "Log Out"))
    ))
    print("✅ Login successful!")

    # --- Repeat payments ---
    for i in range(NUM_PAYMENTS):
        print(f"[INFO] Starting payment #{i+1}...")

        # Always go back to Bill Pay page
        bill_pay_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Bill Pay")))
        actions = ActionChains(driver)
        actions.move_to_element(bill_pay_link).click().perform()

        # Fill out form with fresh random data
        random_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        driver.find_element(By.NAME, "payee.name").send_keys(random_name)
        driver.find_element(By.NAME, "payee.address.street").send_keys(random.choice(address))
        driver.find_element(By.NAME, "payee.address.city").send_keys(random.choice(city))
        driver.find_element(By.NAME, "payee.address.state").send_keys(random.choice(state))
        driver.find_element(By.NAME, "payee.address.zipCode").send_keys(str(random.choice(zip_code)))
        driver.find_element(By.NAME, "payee.phoneNumber").send_keys(str(random.choice(phone_number)))
        driver.find_element(By.NAME, "payee.accountNumber").send_keys(str(account_number))
        driver.find_element(By.NAME, "verifyAccount").send_keys(str(account_number))
        driver.find_element(By.NAME, "amount").send_keys(str(random.choice(amounts)))

        # Submit payment
        payment_btn = driver.find_element(By.CSS_SELECTOR, "input.button[value='Send Payment']")
        time.sleep(1)
        payment_btn.click()

        print(f"✅ Payment #{i+1} submitted.")
        time.sleep(2)  # wait briefly for success message before next loop

    print("🎉 All bulk payments completed.")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    driver.quit()
