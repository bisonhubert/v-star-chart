from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select

url = 'https://justastrologythings.com/pages/chart/index.php'


browser = Firefox()
browser.get(url)

class PageObj:
    month = Select(browser.find_element_by_name('month'))
    day = Select(browser.find_element_by_name('day'))
    year = Select(browser.find_element_by_name('year'))
    hour = Select(browser.find_element_by_name('hour'))
    minute = Select(browser.find_element_by_name('minute'))
    location = browser.find_element_by_id('search')
    submit = browser.find_elements("xpath", '//button')[0]

    def _set_month(self):
        self.month.select_by_index(2)

    def _set_day(self):
        self.day.select_by_index(22)

    def _set_year(self):
        self.year.select_by_index(36)
    #
    # def _set_hour(self, hour=None):
    #     self.hour.select_by_index(36)
    #
    # def _set_minute(self):
    #     self.minute.select_by_index(36)

    def _set_location(self):
        self.location.send_keys("Galveston")

    def run(self, hours=None, minutes=None):
        self._set_month()
        self._set_day()
        self._set_year()
        self._set_location()
        import pdb;pdb.set_trace()
        self.submit.submit()
        # self._set_hour()
        # self._set_minute()

PageObj().run()
import pdb;pdb.set_trace()
