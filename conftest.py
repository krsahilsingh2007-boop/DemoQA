# conftest.py
import os
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=os.environ.get("BROWSER", "brave"),
        help="Browser to run tests on: chrome or brave (default: brave)",
    )


def find_brave_binary():
    paths = [
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe"),
    ]
    for p in paths:
        if os.path.exists(p):
            return p
    return shutil.which("brave.exe")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser", default="brave").lower()
    options = Options()
    options.add_argument("--start-maximized")

    if browser == "brave":
        brave_path = find_brave_binary()
        if not brave_path:
            raise FileNotFoundError("Brave browser executable not found.")
        options.binary_location = brave_path

    # Uncomment below for headless mode
    # options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
