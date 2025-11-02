from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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

# -------------- Step - 2  Automated login -----------------
wait = WebDriverWait(driver, 2)

login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.clear()

# fill in login form
email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

# click login 
submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()

# wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))


#---------------- Step - 3 Book a class ----------------- 
class_cards = driver.find_element(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains@id, 'day-group-']")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # check if this is a tuesday
    if "Tue" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

        if "6.00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button.click()

            print(f"Booked: {class_name} on {day_title}")



