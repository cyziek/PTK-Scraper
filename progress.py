import requests
import json

file_path = "progress.json"
links_file = 'links.txt'
progress_file = 'progress.json'


def load_links():
    with open(links_file, 'r', encoding="utf-8") as file:
        links = file.read().splitlines()
    return links


def save_progress(link_index, curr_page, total_pages):
    progress_data = {
        "link_index": link_index,
        "curr_page": curr_page,
        "total_pages": total_pages
    }
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(progress_data, file)


def load_progress():
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            progress_data = json.load(file)
            return progress_data['link_index'], progress_data['curr_page'], progress_data['total_pages']
    except (FileNotFoundError, KeyError):
        save_progress(0,1,0)
        return 0, 1, 0
    # Start from the first URL and first pagination page

