# File: test_tooltip_doubleclick.py
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_tooltip_double_click(driver):
    driver.get("https://demoqa.com/buttons")
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "doubleClickBtn"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    time.sleep(0.5)
    ActionChains(driver).double_click(button).perform()
    # Wait for the success message to appear after double-click
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "doubleClickMessage"))
    )
    assert "You have done a double click" in message.text
