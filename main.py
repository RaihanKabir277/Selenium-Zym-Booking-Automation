from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Create Chrome Profile and create account manually. Put YOUR email and password here:
ACCOUNT_EMAIL = " "
ACCOUNT_PASSWORD = " "
GYM_URL = "https://appbrewery.github.io/gym/"

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=GYM_URL)



