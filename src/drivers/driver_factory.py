from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from src.config.settings import HEADLESS, PAGE_LOAD_TIMEOUT


def create_driver(browser: str = "chrome"):
    browser = browser.lower()

    if browser == "chrome":
        options = ChromeOptions()

        if HEADLESS:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()

        if HEADLESS:
            options.add_argument("-headless")

        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(
            f"Unsupported browser: {browser}. "
            "Supported browsers: chrome, firefox."
        )

    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    driver.maximize_window()

    return driver
