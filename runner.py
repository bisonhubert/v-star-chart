from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")

from driver import PageObj

page_obj = PageObj(url='https://astrolibrary.org/free-birth-chart/').run()
import pdb;pdb.set_trace()
