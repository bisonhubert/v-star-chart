from driver import PageObj
from parser import Parser

page_obj = PageObj(url='https://astrolibrary.org/free-birth-chart/').run()
parser = Parser(html=page_obj.report_html).run()
page_obj.browser.close()

import pdb;pdb.set_trace()
