from selenium.webdriver.common.by import By
import time

def test_datepicker(driver):
    driver.get("https://demoqa.com/date-picker")
    date_input = driver.find_element(By.ID, "datePickerMonthYearInput")
    date_input.clear()
    date_input.send_keys("08/25/2025")
    time.sleep(1)
    assert "2025" in date_input.get_attribute("value")
