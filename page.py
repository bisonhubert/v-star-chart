import time

from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.support.select import Select


class Page:
    def __init__(self, url=None):
        self.url = url
        self.browser = None
        self.report = None  # selenium WebElement obj
        self.report_html = None  # selenium WebElement innerHTML

    def _set_name(self):
        name = self.browser.find_element_by_id("name")
        name.send_keys("Vanessa")

    def _set_month(self, month=3):
        month_selector = Select(self.browser.find_element_by_id("month"))
        month_selector.select_by_index(month)

    def _set_day(self, day=23):
        day_selector = Select(self.browser.find_element_by_id("day"))
        day_selector.select_by_index(day)

    def _set_year(self):
        year = self.browser.find_element_by_id("year")
        year.send_keys("1989")

    def _set_hour(self, hour=None):
        # hours are 1-indexed in the form
        if hour is None:
            hour = 1
        else:
            hour += 1
        hour_selector = Select(self.browser.find_element_by_id("hour"))
        hour_selector.select_by_index(hour)

    def _set_minute(self, minute=None):
        # minutes are 1-indexed in the form
        if minute is None:
            minute = 1
        else:
            minute += 1
        minute_selector = Select(self.browser.find_element_by_id("minute"))
        minute_selector.select_by_index(minute)

    def _set_location(self):
        location = self.browser.find_element_by_id("placein")
        location.send_keys("Galveston")
        time.sleep(2)
        location_results = self.browser.find_element_by_id("autoComplete_results_list")
        location_results.find_elements("tag name", "li")[0].click()

    def _submit(self):
        submit = self.browser.find_element_by_id("z-fetch-report")
        submit.click()
        time.sleep(1)

    def _get_page(self):
        options = FirefoxOptions()
        options.headless = True
        self.browser = Firefox(options=options)
        self.browser.get(self.url)

    def _set_report(self):
        report = self.browser.find_element("id", "zp-report-content")
        self.report = report
        self.report_html = report.get_attribute("innerHTML")

    def _close_browser(self):
        self.browser.close()

    def run(self, hour=None, minute=None):
        self._get_page()
        self._set_name()
        self._set_month()
        self._set_day()
        self._set_year()
        self._set_hour(hour=hour)
        self._set_minute(minute=minute)
        self._set_location()
        self._submit()
        self._set_report()
        self._close_browser()
        return self
