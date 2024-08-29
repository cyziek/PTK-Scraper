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
        return 0, 0, 0
    # Start from the first URL and first pagination page


def scrape_page(url):
    response = requests.get(url)
    # Process the response as needed
    print(f"Scraped {url}: {response.status_code}")  # Example output


def scrape_paginated(url, start_page=1):
    page = start_page
    while True:
        paginated_url = f"{url}?page={page}"
        scrape_page(paginated_url)

        # Here, you should implement logic to check if there is a next page.
        # This is typically done by inspecting the content of the page or a next-page button.

        # For this example, we'll assume a simple condition:
        has_more_pages = page < 5  # Replace with your actual condition

        if not has_more_pages:
            break
        page += 1

    return page  # Return the last page number scraped
