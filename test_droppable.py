# File: test_droppable.py
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_droppable_element(driver):
    driver.get("https://demoqa.com/droppable/")

    # Remove overlay ads that could intercept mouse events
    driver.execute_script("""
        const ban = document.getElementById('fixedban');
        if (ban) ban.remove();
        const ads = document.querySelectorAll('iframe, [id^=google_ads]');
        ads.forEach(e => e.remove());
    """)

    drag = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "draggable"))
    )
    drop = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#simpleDropContainer #droppable"))
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drop)
    time.sleep(0.5)

    try:
        ActionChains(driver).drag_and_drop(drag, drop).perform()
        WebDriverWait(driver, 3).until(lambda d: "Dropped!" in drop.text)
    except Exception:
        loc_drag = drag.location
        loc_drop = drop.location
        dx = loc_drop["x"] - loc_drag["x"] + 20
        dy = loc_drop["y"] - loc_drag["y"] + 20
        ActionChains(driver).click_and_hold(drag).pause(0.2).move_by_offset(dx, dy).pause(0.2).release().perform()
        WebDriverWait(driver, 5).until(lambda d: "Dropped!" in drop.text)

    assert "Dropped!" in drop.text
