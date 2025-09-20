# Parabank---test-automation

This repository contains **Selenium-based automation scripts** designed to simulate various user actions on the [Parabank](https://parabank.parasoft.com/parabank/index.htm) demo banking site.  
These scripts are useful for **testing, automation practice, and QA scenarios**, such as bulk bill payments, fund transfers, and account registration.

---

## 📂 Project Structure

| File Name         | Description                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------|
| **billpay.py**    | Automates multiple **Bill Payments** with randomized payee information to simulate bulk transactions. |
| **fundtransfer.py** | Logs in and performs a series of **fund transfers** with varying amounts.                  |
| **registration.py** | Automates **new user registration** by creating multiple accounts with random details.     |

---

## ⚡ Features

### ✅ billpay.py
- Logs in with predefined credentials.
- Navigates to the **Bill Pay** page.
- Randomly generates payee names, addresses, and amounts.
- Repeats the payment process multiple times (`NUM_PAYMENTS` configurable).

### ✅ fundtransfer.py
- Logs in with predefined credentials.
- Navigates to the **Transfer Funds** page.
- Executes multiple transfers using a list of preset amounts.

### ✅ registration.py
- Registers multiple new accounts (`Num_Reg` configurable).
- Randomizes user details (name, address, phone, SSN) for each registration.
- Automatically increments usernames (`test1`, `test2`, …).

---

## 🛠️ Requirements

- **Python 3.8+**
- **Google Chrome Browser**
- **ChromeDriver** (matching your Chrome version)
- Required Python package:
  ```bash
  pip install selenium

  🚀 Setup & Usage
**1️⃣ Clone this repository**

`git clone https://github.com/<your-username>/Parabank---test-automation.git`
`cd Parabank---test-automation`

**2️⃣ Install dependencies**
`pip install selenium`

**3️⃣ Download and place ChromeDriver**

**Download ChromeDriver**
  matching your Chrome version.
  Place it in the project directory or specify its path in the script:
  CHROMEDRIVER_PATH = "chromedriver.exe"

**4️⃣ Edit Configurations (Optional)**

Each script includes configurable variables at the top:
  `USERNAME, PASSWORD` (login credentials)
  `NUM_PAYMENTS / Num_Reg` (loop counts)
  Randomized data arrays (names, cities, amounts, etc.)

**5️⃣ Run a script**
  `python billpay.py`
 `python fundtransfer.py`
  `python registration.py`

**🧪 Notes**

  The Parabank site is a public demo, so data resets periodically.
  Scripts are intended for testing and educational purposes only.
  Use the --headless=new Chrome option if you want to run the scripts without opening a browser window:
  options.add_argument("--headless=new")

**💡 Tips**
Increase WAIT_SECONDS if you have a slow internet connection.
Use a virtual environment (venv) to keep dependencies isolated:
  `python -m venv venv`
  `source venv/bin/activate`   # Mac/Linux
  `venv\Scripts\activate`      # Windows

**📜 License**

_This project is provided for educational and testing purposes.
Please use responsibly and avoid running excessive automation on shared servers._

