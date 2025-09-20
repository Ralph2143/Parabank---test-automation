# Parabank Automation Scripts

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
- Required Python packages:
  ```bash
  pip install selenium
