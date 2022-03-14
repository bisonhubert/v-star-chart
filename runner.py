import time

from page import Page
from parser import PlanetParser

HOURS = list(range(12, 16))
MINUTES = list(range(1, 61))
URL = "https://astrolibrary.org/free-birth-chart/"
# test with these settings
# HOURS = list(range(12, 14))
# MINUTES = list(range(1, 3))


class Runner:
    FILEPATH = "charts"
    EXTENSION = "md"

    def __init__(self, hours=None, minutes=None):
        self.hours = None if hours is None else hours
        self.minutes = None if minutes is None else minutes

    def _make_files(self, hour=None, minute=None, planets=None):
        if planets is None:
            return
        timestamp = ""
        if hour is not None and minute is not None:
            # hour and minute are indexed for page selector
            # formatting for actual hour/minute
            # ie: if hour = 12, hour = 11AM
            timestamp = f"{hour-1:02}{minute-1:02}"
        for planet in planets:
            filename = f"{timestamp}_{planet.get('name')}.{self.EXTENSION}"
            f = open(f"{self.FILEPATH}/{filename}", "w")
            f.write(planet.get("content"))
            f.close()

    def run(self, url=None):
        if url is None:
            return self
        for hour in self.hours:
            for minute in self.minutes:
                page = Page(url=url).run(hour=hour, minute=minute)
                parser = PlanetParser(html=page.report_html).run()
                self._make_files(hour=hour, minute=minute, planets=parser.planets)
        return self


print(f"Start time: {time.asctime()}")
runner = Runner(hours=HOURS, minutes=MINUTES).run(url=URL)
print(f"End time: {time.asctime()}")
