from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkboxes(driver):
    driver.get("https://demoqa.com/checkbox")
    # Wait for the tree to load before interacting (supports rc-tree and legacy rct classes)
    switcher = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".rc-tree-switcher, .rct-collapse-btn"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", switcher)
    switcher.click()

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".rc-tree-checkbox, .rct-checkbox"))
    )
    checkbox.click()

    WebDriverWait(driver, 10).until(
        lambda d: "You have selected" in d.page_source
    )
    assert "You have selected" in driver.page_source

