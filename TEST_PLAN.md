# Parabank Automation Test Plan-

## 1. Overview

This project contains automated QA scripts for the Parabank demo banking site.
The scripts demonstrate bulk user actions and data logging using Python, Selenium WebDriver, and OpenPyXL.

| Script                              | Purpose                                                     | Output                     |
| ----------------------------------- | ----------------------------------------------------------- | -------------------------- |
| **parabank_register_save.py**       | Registers multiple new user accounts with randomized data   | `registered_accounts.xlsx` |
| **parabank_bulk_payments_excel.py** | Performs repeated bill-pay transactions and records details | `payments.xlsx`            |
| **parabank_transfer_random.py**     | Executes multiple random fund transfers between accounts    | `fund_transfers.xlsx`      |


## 2. Test Objectives

-Verify that key Parabank features (registration, bill pay, transfers) accept valid data and process transactions.
-Demonstrate automated data entry, navigation, and result logging.
-Capture output data for analysis and reporting.

## 3. Scope

In Scope

-Web UI workflows listed above on the public Parabank demo site.
-Data logging to Excel.
-Basic verification (page loads, success messages).

Out of Scope

-Backend validation of actual banking logic.
-Performance, security, or penetration testing.


## 4. Test Environment

| Component | Details                                              |
| --------- | ---------------------------------------------------- |
| Browser   | Chrome (latest stable)                               |
| Driver    | `chromedriver.exe` matching installed Chrome version |
| OS        | Windows 10/11                                        |
| Python    | 3.10+                                                |
| Libraries | `selenium`, `openpyxl`                               |

## 5. Test Data

User details: Randomized first/last names, addresses, phone numbers, SSNs, usernames with numeric suffix.

Payments/Transfers: Random amounts within predefined ranges.

## 6. Test Scenarios

| ID     | Script                            | Scenario                     | Expected Result                                                                |
| ------ | --------------------------------- | ---------------------------- | ------------------------------------------------------------------------------ |
| REG-01 | `parabank_register_save.py`       | Register 30 unique users     | Each registration completes without error; Excel file contains 30 rows of data |
| PAY-01 | `parabank_bulk_payments_excel.py` | Perform 100 bill payments    | Each payment confirms success; Excel logs payment#, name, amount, timestamp    |
| TRF-01 | `parabank_transfer_random.py`     | Perform 100 random transfers | Each transfer confirms success; Excel logs timestamp and amount                |

## 7. Execution Steps

 1.Install dependencies:

`pip install selenium openpyxl`

 2.Download and match the correct chromedriver.exe to your Chrome version.
 3.Update config values inside each script if needed (paths, run counts, credentials).
 4.Run scripts individually:

<pre> ```python # parabank_register_save.py # ``` </pre>
`python parabank_bulk_payments_excel.py`
`python parabank_transfer_random.py`

 5.Inspect generated Excel files for logged results.**

## 8. Pass/Fail Criteria

-Pass: Script executes all iterations without unhandled exceptions and logs all records to Excel.
-Fail: Script crashes, fails to log data, or produces incomplete Excel files.


## 9. Reporting

-Excel workbooks serve as execution evidence.
-Console output provides run status and errors.

## 10. Maintenance

-Update chromedriver.exe when Chrome updates.
-Adjust element locators if Parabank UI changes.
-Tune run counts or data ranges for load demonstrations.
