# File: test_dialog.py
from selenium.webdriver.common.by import By
import time

def test_modal_dialog(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    driver.find_element(By.ID, "showSmallModal").click()
    time.sleep(1)
    modal = driver.find_element(By.ID, "example-modal-sizes-title-sm")
    assert modal.text == "Small Modal"
    driver.find_element(By.ID, "closeSmallModal").click()
