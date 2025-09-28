# parabank_transfer_random.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, random, openpyxl
from openpyxl import Workbook
from datetime import datetime

# ---- Config ----
CHROMEDRIVER_PATH = "chromedriver.exe"   # update to full path if needed
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
USERNAME = "test1"
PASSWORD = "Th15!s4T3st"
WAIT_SECONDS = 10
RUN_COUNT = 100                            # <---- change this to control number of transfers
EXCEL_FILE = "fund_transfers.xlsx"

# ---- Excel setup ----
try:
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active
except FileNotFoundError:
    wb = Workbook()
    ws = wb.active
    ws.append(["Timestamp", "Transfer Amount"])

# ---- WebDriver setup ----
service = Service(executable_path=CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, WAIT_SECONDS)

try:
    print("[INFO] Opening Parabank...")
    driver.get(BASE_URL)

    print("[INFO] Logging in...")
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

    # Go to Transfer Funds page
    transfer_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds")))
    ActionChains(driver).move_to_element(transfer_link).click().perform()

    # ---- Perform Transfers ----
    for i in range(RUN_COUNT):
        amount = random.randint(1, 10000)
        print(f"[INFO] Run {i+1}/{RUN_COUNT}: transferring {amount}")

        amount_field = wait.until(EC.presence_of_element_located((By.ID, "amount")))
        amount_field.clear()
        amount_field.send_keys(str(amount))

        transfer_btn = driver.find_element(By.CSS_SELECTOR, "input.button[value='Transfer']")
        time.sleep(1)
        transfer_btn.click()

        # log to Excel
        ws.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount])
        wb.save(EXCEL_FILE)

        # wait and return to Transfer Funds page
        time.sleep(2)
        transfer_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds")))
        ActionChains(driver).move_to_element(transfer_link).click().perform()

    print("✅ All transfers completed and saved to Excel.")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    wb.save(EXCEL_FILE)
    driver.quit()
