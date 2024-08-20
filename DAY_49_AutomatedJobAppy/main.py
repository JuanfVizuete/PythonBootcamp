from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PWD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option ("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3996512059&f_AL=true&geoId=106373116&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

time.sleep(2)
sign_in_btn = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_btn.click()
time.sleep(2)

email_box = driver.find_element(By.NAME, "session_key")
email_box.send_keys(EMAIL)
password_box = driver.find_element(By.NAME, "session_password")
password_box.send_keys(PASSWORD, Keys.ENTER)
input("Press Enter to continue after the MFA verification")


def abort_application():
    try:
        # Click Close Button
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

        time.sleep(2)
        # Click Discard Button
        discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[0]
        discard_button.click()
    except NoSuchElementException:
        print("No Easy Apply button, skipped.")
        pass


def apply_job():
    try:
        time.sleep(1)
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_button.click()
        time.sleep(2)

        phone_box = driver.find_element(By.ID, "single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989892611-9-phoneNumber-nationalNumber")
        phone_box.clear()
        phone_box.send_keys(PHONE_NUMBER)
        time.sleep(1)
        submit_btn = driver.find_element(By.CLASS_NAME, 'artdeco-button')
        if submit_btn.get_attribute("aria-label") == "Continue to next step":
            abort_application()
            print("Complex application, skipped.")
            pass

        else:
            input("Press Enter to continue after selecting the correct Resume")  # This is optional for me because I wanted to select another one
            time.sleep(1)
            submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
            submit_btn.click()
            print("Job applied successfully!")

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        pass


all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    apply_job()






