from page import Page
from parser import PlanetParser

page = Page(url='https://astrolibrary.org/free-birth-chart/').run()
parser = PlanetParser(html=page.report_html).run()
filepath = 'charts'
extension = 'md'

def make_files(planets):
    for planet in planets:
        filename = f"{filepath}/{planet.get('name')}.{extension}"
        f = open(filename, "w")
        f.write(planet.get('content'))
        f.close()

make_files(parser.planets)
import pdb;pdb.set_trace()
