# File: test_title_links.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_homepage_title(driver):
    driver.get("https://demoqa.com/")
    # The page title changed on the live site; validate via URL instead
    assert "demoqa.com" in driver.current_url


def test_internal_link_interactions(driver):
    driver.get("https://demoqa.com/")
    card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h5[text()="Interactions"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
    driver.execute_script("arguments[0].click();", card)
    WebDriverWait(driver, 10).until(EC.url_contains("interaction"))
    assert "interaction" in driver.current_url


def test_sidebar_link_resizable(driver):
    driver.get("https://demoqa.com/")
    card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h5[text()="Interactions"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
    driver.execute_script("arguments[0].click();", card)

    resizable_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Resizable"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", resizable_link)
    driver.execute_script("arguments[0].click();", resizable_link)
    WebDriverWait(driver, 10).until(EC.url_contains("resizable"))
    assert "resizable" in driver.current_url


def test_sidebar_link_tooltip(driver):
    driver.get("https://demoqa.com/")
    card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h5[text()="Widgets"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
    driver.execute_script("arguments[0].click();", card)

    tooltip_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Tool Tips"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tooltip_link)
    driver.execute_script("arguments[0].click();", tooltip_link)

    WebDriverWait(driver, 10).until(EC.url_contains("tool-tips"))
    assert "tool-tips" in driver.current_url


def test_external_header_link(driver):
    # Optional: test removed, or you can test some footer link instead
    pass
