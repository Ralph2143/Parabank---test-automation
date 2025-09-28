# parabank_register_save.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random, openpyxl
from openpyxl import Workbook

# ---- Config ----
Num_Reg = 30
name = ["David", "Barnes", "Michael", "Connor", "Blake", "John"]
last_name = ["Smith", "Tailor", "Books", "Gates"]
address = ["Willowbrook", "Stonehaven", "Greenfield", "Oakridge",
           "Silvermere", "Thornbury", "Rivermist"]
city = ["Eastbridge", "Silverpoint", "Grandchester", "Ironvale",
        "Brookhaven", "Ashwick", "Rivergate"]
state = ["Silvermont", "Westoria", "Ashlandia", "Crestwood"]
zip_code = ["3100", "2300", "3400", "4555", "6000", "5560", "3245"]
phone_number = ["33232145100", "23546456400", "34745745700",
                "4557678678675", "609679769600",
                "5566796796790", "3267967969645"]
SSN = ["123-45-6789", "402-18-9365", "591-72-3840",
       "314-29-8751", "278-63-1904", "809-54-2317",
       "667-41-5098", "503-82-7642", "745-19-6203", "386-27-4510"]

password = "Th15!s4T3st"
base_username = "test"

CHROMEDRIVER_PATH = "chromedriver.exe"
BASE_URL = "https://parabank.parasoft.com/parabank/register.htm"
WAIT_SECONDS = 10
EXCEL_FILE = "registered_accounts.xlsx"

# ---- Excel Setup ----
try:
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active
except FileNotFoundError:
    wb = Workbook()
    ws = wb.active
    ws.append([
        "Username", "Password", "First Name", "Last Name", "Address",
        "City", "State", "Zip Code", "Phone Number", "SSN"
    ])

# ---- Selenium Setup ----
service = Service(executable_path=CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")  # uncomment for headless run
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, WAIT_SECONDS)

try:
    for i in range(Num_Reg):
        driver.get(BASE_URL)

        # Randomize details
        first = random.choice(name)
        last = random.choice(last_name)
        addr = random.choice(address)
        cty = random.choice(city)
        st = random.choice(state)
        zipc = random.choice(zip_code)
        phone = random.choice(phone_number)
        ssn = random.choice(SSN)
        new_username = f"{base_username}{i + 1}"

        # Fill form
        wait.until(EC.visibility_of_element_located((By.NAME, "customer.firstName"))).send_keys(first)
        driver.find_element(By.NAME, "customer.lastName").send_keys(last)
        driver.find_element(By.NAME, "customer.address.street").send_keys(addr)
        driver.find_element(By.NAME, "customer.address.city").send_keys(cty)
        driver.find_element(By.NAME, "customer.address.state").send_keys(st)
        driver.find_element(By.NAME, "customer.address.zipCode").send_keys(zipc)
        driver.find_element(By.NAME, "customer.phoneNumber").send_keys(phone)
        driver.find_element(By.NAME, "customer.ssn").send_keys(ssn)
        driver.find_element(By.NAME, "customer.username").send_keys(new_username)
        driver.find_element(By.NAME, "customer.password").send_keys(password)
        driver.find_element(By.NAME, "repeatedPassword").send_keys(password)

        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.button[value='Register']").click()
        print(f"✅ Registration completed for username: {new_username}")

        # Save to Excel
        ws.append([new_username, password, first, last, addr, cty, st, zipc, phone, ssn])
        wb.save(EXCEL_FILE)

        time.sleep(2)

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    wb.save(EXCEL_FILE)
    driver.quit()
