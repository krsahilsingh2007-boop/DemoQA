# File: test_keyboard_events.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_keyboard_event_input(driver):
    driver.get("https://demoqa.com/auto-complete")
    input_box = driver.find_element(By.ID, "autoCompleteMultipleInput")
    input_box.send_keys("Red")
    time.sleep(1)
    input_box.send_keys(Keys.ENTER)
    input_box.send_keys("Green")
    time.sleep(1)
    input_box.send_keys(Keys.ENTER)
    assert "Red" in driver.page_source and "Green" in driver.page_source
