import pprint
import time

from page import Page
from parser import PlanetParser

pp = pprint.PrettyPrinter(indent=2)

HOURS = list(range(11, 17))  # 11AM - 5PM
MINUTES = list(range(0, 60))  # every minute
# test with these settings
# HOURS = list(range(11, 13))
# MINUTES = list(range(0, 2))
URL = "https://astrolibrary.org/free-birth-chart/"


class Runner:
    FILEPATH = "charts"
    EXTENSION = "md"

    def __init__(self, hours=None, minutes=None):
        self.hours = None if hours is None else hours
        self.minutes = None if minutes is None else minutes
        self.tracker = None 

    def _update_tracker(self, content):
        heading = content.split('\n')[0].strip()
        planet = heading.split(' ')[0].lower() 
        point = heading.split(' ')[-1].lower() 
        if self.tracker is None:
            self.tracker = []
        base_tracker = {
            'planet': planet,
            'point': {point},
            'has_multi_point': False,
            'has_multi_points': False,
            'point_tracker': {point: 1}
        }
        current_tracker_indx = None
        for indx, tracker in enumerate(self.tracker):
            if tracker['planet'] == planet:
                base_tracker = tracker
                current_tracker_indx = indx
        if current_tracker_indx is None:
            self.tracker.append(base_tracker)
        else:
            base_tracker['point'].add(point)
            if point in base_tracker['point_tracker']:
                base_tracker['point_tracker'][point] += 1
            else:
                base_tracker['point_tracker'][point] = 1
            base_tracker['has_multi_point'] = len(base_tracker['point']) > 1
            base_tracker['has_multi_points'] = len(base_tracker['point_tracker'].keys()) > 1
            self.tracker[current_tracker_indx] = base_tracker

    def _make_files(self, hour=None, minute=None, planets=None):
        if planets is None:
            return
        timestamp = ""
        if hour is not None and minute is not None:
            timestamp = f"{hour:02}{minute:02}"
        for planet in planets:
            filename = f"{timestamp}_{planet.get('name')}.{self.EXTENSION}"
            f = open(f"{self.FILEPATH}/{filename}", "w")
            content = planet.get('content')
            f.write(content)
            f.close()
            self._update_tracker(content)

    def _make_tracker_file(self):
        content = None
        f = open('tracker.md', 'w')
        for planet in self.tracker: 
            content = f"Planet: {planet['planet']}\n"
            content = f"{content}Point: {planet['point']}\n"
            content = f"{content}Point Tracker: {planet['point_tracker']}\n\n"
            f.write(content)
        f.close()

    def run(self, url=None):
        if url is None:
            return self
        for hour in self.hours:
            for minute in self.minutes:
                page = Page(url=url).run(hour=hour, minute=minute)
                parser = PlanetParser(html=page.report_html).run()
                self._make_files(hour=hour, minute=minute, planets=parser.planets)
        self._make_tracker_file()
        return self


print(f"Start time: {time.asctime()}")
runner = Runner(hours=HOURS, minutes=MINUTES).run(url=URL)
print(f"End time: {time.asctime()}")
