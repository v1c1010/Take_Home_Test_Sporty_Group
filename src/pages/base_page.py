from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config.settings import EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def open(self, url):
        self.driver.get(url)

    def wait_for_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_present(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def is_visible(self, locator):
        try:
            return self.wait_for_visible(locator).is_displayed()
        except Exception:
            return False

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
