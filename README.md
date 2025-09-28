# Parabank---test-automation

This repository contains **Selenium-based automation scripts** that simulate key user actions on the [Parabank](https://parabank.parasoft.com/parabank/index.htm) demo banking site.  
The scripts are designed for **testing, QA practice, and automation learning**, including bill payments, fund transfers, and bulk account registration.

---

## 📂 Project Structure

| File Name               | Description                                                                                             |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| **billpay.py**           | Automates **Bill Payments** with randomized payee details and logs each successful transaction to `payments.xlsx`. |
| **fundtransfer.py**      | Logs in, performs **fund transfers** using random amounts (1–10,000), and records each transfer to `fund_transfers.xlsx`. |
| **registration.py**      | Automates **new user registrations** and saves every created account (username, password, and details) to `registered_accounts.xlsx`. |

---

## ⚡ Features

### ✅ billpay.py
- Logs in with predefined credentials.
- Navigates to **Bill Pay**.
- Randomly generates payee names, addresses, and payment amounts.
- Repeats the payment process a configurable number of times (`NUM_PAYMENTS`).
- **Automatically logs each successful payment** (name, amount, etc.) to an Excel file (`payments.xlsx`).

### ✅ fundtransfer.py
- Logs in with predefined credentials.
- Navigates to **Transfer Funds**.
- Executes a configurable number of transfers (`NUM_TRANSFERS`).
- Chooses a **random amount between 1 and 10,000** for each transfer.
- **Logs every transfer** (timestamp, amount, and status) to `fund_transfers.xlsx`.

### ✅ registration.py
- Creates multiple **new user accounts** (`Num_Reg` configurable).
- Randomizes all user details (name, address, phone, SSN) for each registration.
- Automatically increments usernames (e.g., `test1`, `test2`, …).
- **Saves all registered account data** (username, password, and all form fields) to `registered_accounts.xlsx`.

---

## 🧪 Notes
- Parabank is a **public demo site**; data resets periodically.
- These scripts are **for testing and educational use only**.
- To run without opening a browser window, enable headless mode:
  ```python
  options.add_argument("--headless=new")


**💡 Tips**
Increase WAIT_SECONDS if you have a slow internet connection.
Use a virtual environment (venv) to keep dependencies isolated:
  `python -m venv venv`
 `source venv/bin/activate`  # Mac/Linux
  `venv\Scripts\activate`     # Windows

**📜 License**

_This project is provided for educational and testing purposes.
Please use responsibly and avoid running excessive automation on shared servers._


## 🛠️ Requirements

- **Python 3.8+**
- **Google Chrome Browser**
- **ChromeDriver** (matching your Chrome version)
- Required Python package:
  ```bash
  pip install selenium openpyxl 

**  🚀 Setup & Usage**

**1️⃣ Clone this repository**

`git clone https://github.com/<your-username>/Parabank---test-automation.git`
`cd Parabank---test-automation`

**2️⃣ Install dependencies**
`pip install selenium openpyxl`

**3️⃣ Download and place ChromeDriver**

**Download ChromeDriver**
  matching your Chrome version.
  Place it in the project directory or specify its path in the script:
  CHROMEDRIVER_PATH = "chromedriver.exe"

**4️⃣ Edit Configurations (Optional)**

Each script includes configurable variables at the top:
  `USERNAME, PASSWORD` (login credentials)
  `NUM_PAYMENTS / NUM_TRANSFERS / Num_Reg` (loop counts)
  Randomized data arrays (names, cities, etc.)

**5️⃣ Run a script**
```bash
  python billpay.py
  python fundtransfer.py
  python registration.py

The output Excel files (payments.xlsx, fund_transfers.xlsx, registered_accounts.xlsx) will be created/updated automatically in the project directory.


This version reflects:
- **Excel logging** in all scripts.
- **Random transfer amounts** with adjustable run counts.
- Clear instructions for dependencies (`selenium`, `openpyxl`).


