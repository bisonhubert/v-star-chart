import requests
from bs4 import BeautifulSoup

url = 'https://justastrologythings.com/pages/chart/index.php'
params = 'googleLat=29.2366&googleLng=-94.8688828&googleLocation=Galveston&name=&month=1&day=1&year=2000&hour=12&minute=00&submitted=TRUE'

resp = requests.get(f'{url}?{params}')
parser = BeautifulSoup(resp.content, "html.parser")

import pdb;pdb.set_trace()
