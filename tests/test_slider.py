# File: test_slider.py
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_slider_movement(driver):
    driver.get("https://demoqa.com/slider")
    slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.range-slider"))
    )
    slider_value = driver.find_element(By.ID, "sliderValue")

    # Read starting value
    initial_value = int(slider_value.get_attribute("value"))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", slider)
    time.sleep(0.5)

    # Move slider to the right by a significant offset
    ActionChains(driver).click_and_hold(slider).move_by_offset(100, 0).release().perform()
    time.sleep(1)

    new_value = int(slider_value.get_attribute("value"))
    assert new_value > initial_value, f"Slider did not move: {initial_value} -> {new_value}"
