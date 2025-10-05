# parabank_transfer_random.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, random, openpyxl
from openpyxl import Workbook
from datetime import datetime
from login_helper import parabank_login

# ---- Config ----
CHROMEDRIVER_PATH = "chromedriver.exe"
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
WAIT_SECONDS = 10
RUN_COUNT = 100
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
    parabank_login(driver, wait, BASE_URL)  # ✅ Login handled by helper


    transfer_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds")))
    ActionChains(driver).move_to_element(transfer_link).click().perform()

    for i in range(RUN_COUNT):
        amount = random.randint(1, 10000)
        print(f"[INFO] Run {i+1}/{RUN_COUNT}: transferring {amount}")

        amount_field = wait.until(EC.presence_of_element_located((By.ID, "amount")))
        amount_field.clear()
        amount_field.send_keys(str(amount))

        transfer_btn = driver.find_element(By.CSS_SELECTOR, "input.button[value='Transfer']")
        time.sleep(1)
        transfer_btn.click()

        ws.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount])
        wb.save(EXCEL_FILE)

        time.sleep(2)
        transfer_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds")))
        ActionChains(driver).move_to_element(transfer_link).click().perform()

    print("✅ All transfers completed and saved to Excel.")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    wb.save(EXCEL_FILE)
    driver.quit()
