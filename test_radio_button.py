from selenium.webdriver.common.by import By
import time

def test_radiobuttons(driver):
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.XPATH, '//label[text()="Yes"]').click()
    time.sleep(1)
    assert "Yes" in driver.page_source
