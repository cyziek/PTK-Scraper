import api_requests
from api_requests import send_request
from html_parser import *
from progress import *
from cookies import cookies
if __name__ == '__main__':
    links = load_links()
    link_index, curr_page, total_pages = load_progress()

    while link_index <= len(links):
        path = links[link_index]
        response = send_request(path, curr_page)
        total_pages = extract_pages_count(response)
        save_progress(link_index, curr_page, total_pages)
        while curr_page <= total_pages:
            response = send_request(path, curr_page)
            extract_companies_from_html(response)
            curr_page = curr_page + 1
            save_progress(link_index, curr_page, total_pages)
        curr_page = 1
        total_pages = 0
        link_index += 1
        save_progress(link_index, curr_page, total_pages)

