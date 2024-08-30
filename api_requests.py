import requests
from cookies import *
from headers import *
from selenium_auth import *
from bs4 import BeautifulSoup


def send_request(path, page):
    retries = 0;
    response = requests.get(f'https://www.pkt.pl{path}/{page}', cookies=cookies(), headers=headers())
    while retries < 3 and "<title>Potwierdź swoją tożsamość</title>" in response.text:
        if "<title>Potwierdź swoją tożsamość</title>" in response.text:
            selenim_auth()
            retries +=1
            response = requests.get(f'https://www.pkt.pl{path}/{page}', cookies=cookies(), headers=headers())
    return response
