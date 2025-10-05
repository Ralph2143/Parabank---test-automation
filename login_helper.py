# login_helper.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# ---- Credentials (edit here when password changes) ----
USERNAME = "test1"
PASSWORD = "Th15!s4T3st"

def parabank_login(driver, wait, base_url):
    driver.get(base_url)
    
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
