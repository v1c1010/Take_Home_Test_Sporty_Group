import pytest

from src.config.settings import BASE_URL, BROWSER
from src.drivers.driver_factory import create_driver
from src.pages.upcoming_matches_page import UpcomingMatchesPage


@pytest.fixture
def driver():
    driver = create_driver(BROWSER)

    yield driver

    driver.quit()


@pytest.fixture
def main_content(driver):
    page = UpcomingMatchesPage(driver)
    page.load(BASE_URL)

    return page
