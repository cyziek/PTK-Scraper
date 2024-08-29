import api_requests
from api_requests import send_request
from html_parser import parse_html
from cookies import cookies
if __name__ == '__main__':
    response = send_request()
    parse_html(response)
