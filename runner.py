from page import Page
from parser import PlanetParser

# HOUR_RANGE = list(range(12, 25))
# MINUTES = list(range(1, 61))
URL = 'https://astrolibrary.org/free-birth-chart/'
HOURS = list(range(12, 14))
MINUTES = list(range(1, 3))


class Runner:
    FILEPATH = 'charts'
    EXTENSION = 'md'

    def __init__(self, hours=None, minutes=None):
        self.hours = None if hours is None else hours
        self.minutes = None if minutes is None else minutes

    def _make_files(self, hour=None, minute=None, planets=None):
        if planets is None:
            return
        timestamp = ''
        if hour is not None and minute is not None:
            timestamp = f'{hour:02}{minute:02}'
        for planet in planets:
            filename = f"{timestamp}_{planet.get('name')}.{self.EXTENSION}"
            f = open(f"{self.FILEPATH}/{filename}", "w")
            f.write(planet.get('content'))
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


runner = Runner(hours=HOURS, minutes=MINUTES).run(url=URL)
