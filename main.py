import requests
from bs4 import BeautifulSoup

cookies = {
    '__hs_cookie_cat_pref': '1:true,2:true,3:true',
    'cookieConsent': 'ad_storage.granted:analytics_storage.granted:ad_user_data.granted:ad_personalization.granted:functionality_storage.granted:personalization_storage.granted:security_storage.granted',
    '_gcl_au': '1.1.1866373277.1724791973',
    '_gid': 'GA1.2.11813295.1724791973',
    'hubspotutk': '06b9bb4603726391a03521903b84effe',
    '__hssrc': '1',
    'AWSALBAPP-1': '_remove_',
    'AWSALBAPP-2': '_remove_',
    'AWSALBAPP-3': '_remove_',
    '_fbp': 'fb.1.1724792942069.715785648440145320',
    'JSESSIONID': '6A05AE39B01F29CCA69512227CEEC2FA',
    '__hstc': '173540924.06b9bb4603726391a03521903b84effe.1724791973427.1724799127562.1724867540966.4',
    '_ga': 'GA1.2.1947737545.1724791973',
    'AWSALBAPP-0': 'AAAAAAAAAADkFt1XGF9kS2hMt/b63lI+DkD9DuwW7hzin0zDDZWMJOqz98xOJ1OT+Yss1+ikgTM/Ya2Xm1FBBRleUKUFKZJxfKuYz7QrMXk01hUGgmt+QeFQg23Ll+jRF+Ggb+iMBYl4nA==',
    '_gat_UA-25211025-1': '1',
    '_ga_JYXZKDJN52': 'GS1.1.1724867540.4.1.1724869469.0.0.0',
    '__hssc': '173540924.9.1724867540966',
    '_ga_BTHGS94KMP': 'GS1.1.1724867540.4.1.1724869489.40.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__hs_cookie_cat_pref=1:true,2:true,3:true; cookieConsent=ad_storage.granted:analytics_storage.granted:ad_user_data.granted:ad_personalization.granted:functionality_storage.granted:personalization_storage.granted:security_storage.granted; _gcl_au=1.1.1866373277.1724791973; _gid=GA1.2.11813295.1724791973; hubspotutk=06b9bb4603726391a03521903b84effe; __hssrc=1; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; _fbp=fb.1.1724792942069.715785648440145320; JSESSIONID=6A05AE39B01F29CCA69512227CEEC2FA; __hstc=173540924.06b9bb4603726391a03521903b84effe.1724791973427.1724799127562.1724867540966.4; _ga=GA1.2.1947737545.1724791973; AWSALBAPP-0=AAAAAAAAAADkFt1XGF9kS2hMt/b63lI+DkD9DuwW7hzin0zDDZWMJOqz98xOJ1OT+Yss1+ikgTM/Ya2Xm1FBBRleUKUFKZJxfKuYz7QrMXk01hUGgmt+QeFQg23Ll+jRF+Ggb+iMBYl4nA==; _gat_UA-25211025-1=1; _ga_JYXZKDJN52=GS1.1.1724867540.4.1.1724869469.0.0.0; __hssc=173540924.9.1724867540966; _ga_BTHGS94KMP=GS1.1.1724867540.4.1.1724869489.40.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

response = requests.get('https://www.pkt.pl/szukaj/administracja-biur', cookies=cookies, headers=headers)




soup = BeautifulSoup(response.text, 'html.parser')


companies = soup.find_all('div', class_='company-row')

company_data = []

for company in companies:
    # Extract the company name
    name = company.find('h2', class_='company-name').get_text(strip=True) if company.find('h2',
                                                                                          class_='company-name') else None

    # Extract the company category
    category = company.find('div', class_='company-category').get_text(strip=True) if company.find('div',
                                                                                                   class_='company-category') else None

    # Extract the company address
    address = company.find('span', class_='street-address').get_text(strip=True) if company.find('span',
                                                                                                 class_='street-address') else None

    # Extract the phone number
    phone_tag = company.find('span', class_='phone-content')
    phone = phone_tag.get_text(strip=True) if phone_tag else ''

    # Extract the email
    email_tag = company.find('span', title=True)
    email = email_tag['title'] if email_tag and '@' in email_tag['title'] else ''

    # Add the extracted data to the list
    company_data.append({
        'name': name,
        'category': category,
        'address': address,
        'phone': phone,
        'email': email
    })

# Now, 'company_data' contains all the extracted information.
for data in company_data:
    print(data)