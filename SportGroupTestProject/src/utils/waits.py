from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config.settings import EXPLICIT_WAIT


def wait_for_visible(driver, locator, timeout=EXPLICIT_WAIT):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=EXPLICIT_WAIT):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_present(driver, locator, timeout=EXPLICIT_WAIT):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
