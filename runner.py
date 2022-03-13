import time

from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select

url = 'https://astrolibrary.org/free-birth-chart/'


browser = Firefox()
browser.get(url)

class PageObj:
    name = browser.find_element_by_id('name')
    month = Select(browser.find_element_by_id('month'))
    day = Select(browser.find_element_by_id('day'))
    year = browser.find_element_by_id('year')
    hour = Select(browser.find_element_by_id('hour'))
    minute = Select(browser.find_element_by_id('minute'))
    location = browser.find_element_by_id('placein')
    location_results = browser.find_element_by_id('autoComplete_results_list')
    submit = browser.find_element_by_id('z-fetch-report')

    def _set_name(self):
        self.name.send_keys('Vanessa')

    def _set_month(self):
        self.month.select_by_index(3)

    def _set_day(self):
        self.day.select_by_index(23)

    def _set_year(self):
        self.year.send_keys('1989')

    def _set_hour(self, hour=1):
        self.hour.select_by_index(hour)

    def _set_minute(self, minute=1):
        self.minute.select_by_index(minute)

    def _set_location(self):
        self.location.send_keys("Galveston")
        time.sleep(3)
        self.location_results.find_elements_by_tag_name('li')[0].click()

    def run(self, hours=None, minutes=None):
        self._set_name()
        self._set_month()
        self._set_day()
        self._set_year()
        self._set_hour()
        self._set_minute()
        self._set_location()
        self.submit.click()

PageObj().run()
import pdb;pdb.set_trace()
