import requests
from cookies import *
from headers import *
from bs4 import BeautifulSoup


def send_request(path, page):
    response = requests.get(f'https://www.pkt.pl{path}/{page}', cookies=cookies(), headers=headers())
    return response
