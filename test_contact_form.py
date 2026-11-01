# File: test_contact_form.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_submit_contact_form(driver):
    driver.get("https://demoqa.com/text-box")

    # Fill out the form fields
    driver.find_element(By.ID, "userName").send_keys("John Doe")
    driver.find_element(By.ID, "userEmail").send_keys("john@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("123 Street Name")
    driver.find_element(By.ID, "permanentAddress").send_keys("456 Another St")

    # Locate and scroll to submit button
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    # Wait until it's clickable
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit")))

    # Click it
    submit_button.click()

    time.sleep(1)

    # Optional assertions (e.g., checking output below the form)
    output_name = driver.find_element(By.ID, "name").text
    output_email = driver.find_element(By.ID, "email").text

    assert "John Doe" in output_name
    assert "john@example.com" in output_email
