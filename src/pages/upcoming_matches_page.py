from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class UpcomingMatchesPage(BasePage):

    MAIN_CONTENT = (By.ID, "main-content")

    DATE_FILTER = (By.ID, "date-filter")
    DATE_FILTER_POPOVER = (By.ID, "date-filter-popover")
    CALENDAR_GRID = (By.ID, "calendar-grid")
    APPLY_DATE = (By.ID, "apply-date")

    DAY_14 = (
        By.XPATH,
        "//*[@id='calendar-grid']//*[contains(@class, 'dayCell') and normalize-space()='14']"
    )

    DAY_30 = (
        By.XPATH,
        "//*[@id='calendar-grid']//*[contains(@class, 'dayCell') and normalize-space()='30']"
    )

    MATCH_LIST = (By.ID, "match-list")

    def is_match_list_not_empty(self):
        return bool(self.get_text(self.MATCH_LIST).strip())

    def click_date_filter(self):
        self.click(self.DATE_FILTER)

    def is_date_filter_popover_displayed(self):
        return self.is_visible(self.DATE_FILTER_POPOVER)

    def click_calendar_grid(self):
        self.click(self.CALENDAR_GRID)

    def select_day_14(self):
        self.click(self.DAY_14)

    def select_day_30(self):
        self.click(self.DAY_30)

    def apply_date(self):
        self.click(self.APPLY_DATE)

    def load(self, url):
        self.open(url)
        self.wait_for_present(self.MAIN_CONTENT)

    def is_loaded(self):
        return self.is_visible(self.MAIN_CONTENT)

    def get_content_text(self):
        return self.get_text(self.MAIN_CONTENT)


