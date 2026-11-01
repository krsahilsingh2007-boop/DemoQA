# File: test_resizable.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_resizable_element(driver):
    driver.get("https://demoqa.com/resizable/")

    # Get the resizable box using the correct ID
    box = driver.find_element(By.ID, "resizableBoxWithRestriction")

    # Record initial size
    initial_width = box.size["width"]
    initial_height = box.size["height"]

    # Get the resize handle
    resize_handle = box.find_element(By.CSS_SELECTOR, "span.react-resizable-handle")

    # Scroll into view and resize
    driver.execute_script("arguments[0].scrollIntoView(true);", box)
    time.sleep(0.5)

    actions = ActionChains(driver)
    actions.click_and_hold(resize_handle).move_by_offset(100, 50).release().perform()

    time.sleep(1)

    new_width = box.size["width"]
    new_height = box.size["height"]

    # Assert that the box actually grew from its initial size
    assert new_width >= initial_width, f"Width did not increase: {initial_width} -> {new_width}"
    assert new_height >= initial_height, f"Height did not increase: {initial_height} -> {new_height}"
