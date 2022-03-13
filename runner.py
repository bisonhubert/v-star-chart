from page import Page
from parser import PlanetParser


class Runner:
    FILEPATH = 'charts'
    EXTENSION = 'md'

    def __init__(self, url=None):
        self.page = Page(url=url).run()

    def _make_files(self, planets=None):
        if planets is None:
            return
        for planet in planets:
            filename = f"{self.FILEPATH}/{planet.get('name')}.{self.EXTENSION}"
            f = open(filename, "w")
            f.write(planet.get('content'))
            f.close()

    def run(self):
        parser = PlanetParser(html=self.page.report_html).run()
        self._make_files(planets=parser.planets)


runner = Runner(url='https://astrolibrary.org/free-birth-chart/')
runner.run()
