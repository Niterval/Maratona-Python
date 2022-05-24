
import requests
from bs4 import BeautifulSoup

url = 'https://www.iban.com/currency-codes'
r_iban = requests.get(url)
html_iban = r_iban.text

soup = BeautifulSoup(html_iban, 'html.parser')
table = soup.find_all('tr')

negotiation = []

for tr in table:
    info = {
    'country':tr.contents[1].get_text('td'),
    'currency':tr.contents[5].get_text('td')
    }

    tr.find_all('td')

    country = tr.contents[1]
    currency = tr.contents[5]

    if country != '' or currency != '':
        negotiation.append(info)

    # print(negotiation)
