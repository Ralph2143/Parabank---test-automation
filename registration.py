# parabank_login_simple.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

Num_Reg = 5
name = ["David", "Barnes", "Michael", "Connor", "Blake", "John"]
last_name = ["Smith", "Tailor", "Books", "Gates"]
address = ["Willowbrook", "Stonehaven", "Greenfield", "Oakridge",
           "Silvermere", "Thornbury", "Rivermist"]
city = ["Eastbridge", "Silverpoint", "Grandchester", "Ironvale",
        "Brookhaven", "Ashwick", "Rivergate"]
state = ["Silvermont", "Westoria", "Ashlandia", "Crestwood"]
zip_code = ["3100", "2300", "3400", "4555", "6000", "5560", "3245"]  # ✅ strings
phone_number = ["33232145100", "23546456400", "34745745700",
                "4557678678675", "609679769600",
                "5566796796790", "3267967969645"]  # ✅ strings
SSN = ["123-45-6789", "402-18-9365", "591-72-3840",
       "314-29-8751", "278-63-1904", "809-54-2317",
       "667-41-5098", "503-82-7642", "745-19-6203", "386-27-4510"]

password = "Th15!s4T3st"
base_username = "test"   # base name for all usernames

CHROMEDRIVER_PATH = "chromedriver.exe"
BASE_URL = "https://parabank.parasoft.com/parabank/register.htm"
WAIT_SECONDS = 10

service = Service(executable_path=CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")  # run headless if desired
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, WAIT_SECONDS)

try:
    for i in range(Num_Reg):
        driver.get(BASE_URL)

        first_name_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "customer.firstName"))
        )
        first_name_input.send_keys(random.choice(name))
        driver.find_element(By.NAME, "customer.lastName").send_keys(random.choice(last_name))
        driver.find_element(By.NAME, "customer.address.street").send_keys(random.choice(address))
        driver.find_element(By.NAME, "customer.address.city").send_keys(random.choice(city))  # ✅ fixed
        driver.find_element(By.NAME, "customer.address.state").send_keys(random.choice(state))
        driver.find_element(By.NAME, "customer.address.zipCode").send_keys(str(random.choice(zip_code)))  # ✅ ensure string
        driver.find_element(By.NAME, "customer.phoneNumber").send_keys(str(random.choice(phone_number)))  # ✅ ensure string
        driver.find_element(By.NAME, "customer.ssn").send_keys(random.choice(SSN))

        # Increment username per registration
        registration_number = i + 1
        new_username = f"{base_username}{registration_number}"
        driver.find_element(By.NAME, "customer.username").send_keys(new_username)
        driver.find_element(By.NAME, "customer.password").send_keys(password)
        driver.find_element(By.NAME, "repeatedPassword").send_keys(password)

        # Short visual pause (remove or reduce in production)
        time.sleep(1)

        register_btn = driver.find_element(By.CSS_SELECTOR, "input.button[value='Register']")
        register_btn.click()

        print(f"✅ Registration completed for username: {new_username}")

        # Optional wait before next loop
        time.sleep(2)

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    driver.quit()
