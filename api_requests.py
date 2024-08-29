import requests
from cookies import *
from headers import *
from bs4 import BeautifulSoup
def send_request():
    response = requests.get('https://www.pkt.pl/szukaj/administracja-biur', cookies=cookies(), headers=headers())
    return response