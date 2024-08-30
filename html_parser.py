import math

from bs4 import BeautifulSoup

from csv_writer import *


def extract_companies_from_html(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    companies = soup.find_all('div', class_='company-row')

    company_data = []

    for company in companies:
        name = company.find('h2', class_='company-name').get_text(strip=True) if company.find('h2',
                                                                                              class_='company-name') else None
        category = company.find('div', class_='company-category').get_text(strip=True) if company.find('div',
                                                                                                       class_='company-category') else None
        address = company.find('span', class_='street-address').get_text(strip=True) if company.find('span',
                                                                                                     class_='street-address') else None
        phone_tag = company.find('span', class_='phone-content')
        phone = phone_tag.get_text(strip=True) if phone_tag else ''

        email_tag = company.find('span', title=True)
        email = email_tag['title'] if email_tag and '@' in email_tag['title'] else ''

        company_data.append({
            'name': name,
            'category': category,
            'address': address,
            'phone': phone,
            'email': email
        })
        write_csv(str(name)+";"+str(category)+";"+str(address)+";"+str(phone)+";"+str(email)+";"+"\n")
    # for data in company_data:
        # print(data)


def extract_pages_count(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    total_companies_count = soup.find('h1').find('b').text
    total_companies_count = total_companies_count.replace(',', '')
    pages = float(total_companies_count)
    pages = pages/25
    pages = math.ceil(pages)
    if pages > 1000:
        pages = 1000
    return pages