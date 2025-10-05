# Parabank---test-automation

This repository contains **Selenium-based automation scripts** that simulate key user actions on the [Parabank](https://parabank.parasoft.com/parabank/index.htm) demo banking site.  
The scripts are designed for **testing, QA practice, and automation learning**, including bill payments, fund transfers, and bulk account registration.

---

## 📂 Project Structure

| File Name                                                 | Description                                                                                                             |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **`login_helper.py`**                                     | Contains the **reusable login function** and **centralized credentials** for all scripts. Update credentials here only. |
| **`fundtransfer.py`**                                     | Automates **fund transfers** using random amounts and logs results to `fund_transfers.xlsx`.                            |
| **`billpay.py`**                                          | Automates **bulk bill payments** with randomized payee data and logs results to `payments.xlsx`.                        |
| **`registration.py`**                                     | Automates **new user registrations** and saves account info to `registered_accounts.xlsx`.                              |

---

## ⚡ Features

### ✅ billpay.py
- Imports and uses parabank_login() from login_helper.py.
-Automates bulk bill payments to random payees.
-Randomizes names, addresses, and payment amounts.
-Records each payment (number, payee, amount, timestamp) in payments.xlsx.

### ✅ fundtransfer.py
-Imports and uses parabank_login() from login_helper.py.
-Navigates to Transfer Funds and performs a configurable number of transfers.
-Randomizes each transfer amount between 1–10,000.
-Logs every transaction (timestamp + amount) to fund_transfers.xlsx.

### ✅ registration.py
- Creates multiple **new user accounts** (`Num_Reg` configurable).
- Randomizes all user details (name, address, phone, SSN) for each registration.
- Automatically increments usernames (e.g., `test1`, `test2`, …).
- **Saves all registered account data** (username, password, and all form fields) to `registered_accounts.xlsx`.

###✅ login_helper.py

-Centralized credentials for all automation scripts (USERNAME, PASSWORD).
-Exposes a reusable parabank_login(driver, wait, base_url) function.
-Handles login validation automatically.
-Update credentials once here instead of modifying every script.

---
###🧩 How It Works

#### 1. login_helper.py holds the login logic and credentials.
All scripts call:
`from login_helper import parabank_login
parabank_login(driver, wait, BASE_URL)`


#### 2. Once logged in, each script continues its specific workflow — e.g., transfers, payments, or registration.
#### 3. Results are automatically written to Excel files for easy tracking.

### 🧪 Notes

Parabank is a public demo banking site, and data resets periodically.
Scripts are for educational and QA testing purposes only.

To run without showing a browser window (headless mode):
`options.add_argument("--headless=new")`

### ⚙️ Requirements

`Python 3.8+`

`Google Chrome Browser`

`Matching ChromeDriver`

### Dependencies:

`pip install selenium openpyxl`

### 🚀 Setup & Usage
#### 1️⃣ Clone the repository
`git clone https://github.com/<your-username>/Parabank---test-automation.git`
`cd Parabank---test-automation`

#### 2️⃣ Install dependencies
`pip install selenium openpyxl`

#### 3️⃣ Download and place ChromeDriver

Download ChromeDriver that matches your Chrome version.

Place it in the project folder or update this variable in each script:

`CHROMEDRIVER_PATH = "chromedriver.exe"`

#### 4️⃣ Update credentials (if needed)

Edit only login_helper.py:

`USERNAME = "your_username"`
`PASSWORD = "your_password"`

#### 5️⃣ Run the desired script
`python fundtransfer.py`
`python parabank_bulk_payments_excel.py`
`python registration.py`


Excel files (fund_transfers.xlsx, payments.xlsx, registered_accounts.xlsx) will be automatically created or updated in the project directory.

###💡 Tips

Increase WAIT_SECONDS if you have a slower internet connection.

Use a Python virtual environment for isolated dependencies:

`python -m venv venv`
`venv\Scripts\activate`   # Windows
`source venv/bin/activate`  # Mac/Linux

### 📜 License

This project is for educational and testing purposes only.
Do not run excessive automation against public servers.

