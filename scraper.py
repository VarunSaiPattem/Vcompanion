import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import time

load_dotenv()

def login_vtop():
    username = os.getenv("VTOP_USERNAME")
    password = os.getenv("VTOP_PASSWORD")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    driver.get("https://vtop.vitap.ac.in/vtop")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # CAPTCHA can't be auto-filled
    print("Please manually enter the CAPTCHA in the browser window.")
    input("Press Enter after solving CAPTCHA and logging in...")

    time.sleep(5)

    # Assume successful login and extract data
    # TODO: Navigate to pages and scrape actual attendance/schedule

    fake_data = {
        "attendance": [
            {"subject": "MAT1002", "present": "14", "total": "16", "percentage": "87.5%"},
            {"subject": "PHY1701", "present": "12", "total": "14", "percentage": "85.7%"}
        ],
        "schedule": [
            {"time": "09:00 AM", "subject": "MAT1002"},
            {"time": "11:00 AM", "subject": "PHY1701"}
        ]
    }

    driver.quit()
    return fake_data