import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


header = {'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

url_iban = 'https://www.iban.com/currency-codes'
url_wise = 'https://wise.com/gb/currency-converter/'
r_iban = requests.get(url_iban)
html_doc = r_iban.text


def menu_source(msg):
  print(msg)
  try:
    ## Input moeda de origem
    choice = int(input('## -> '))
    if choice > len(country_all):
      print('Nao tem. Escolha um Nº da lista:')
      return menu_source(msg)
    else:
      selected = country_all[choice]
      print(f'\n(x): {selected["name"]}\n')
      print('testando..... 01')

      return menu_amount(money_from, money_to)
      print('testando..... 03')
  except:
      print('Só pode numero. Tente denovo \n')
      print('testando..... 04')


def menu_amount(money_from, money_to):
  try:
    ## Input moeda de destino
    print(f'Quantos {money_from["code"]} você quer converter pra {money_to["code"]}?\n')
    amount = float(input("#: "))
    return amount
  except:
    print("Aqui é permitido apneas numero. Tente denovo \n")
    return menu_amount(money_from, money_to)

## ## SCRAPE IBAN #######
soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')[1:]

country_all = []

for row in rows:
    items = row.find_all('td')
    country = items[0].text
    currency = items[2].text

    if currency == '':
        continue
    else:
        info_country = {
            'name': country.capitalize(),
            'code': currency
        }
        country_all.append(info_country)




print("BEM-VINDO(a)! Escolha pelo número os dois paises\nque você deseja negociar as moeda\n")

for index, info_country in enumerate(country_all):
  print(f"{index} - {info_country['name']}")

# print("\nPelo número, escolha o país de origem da moeda:")

# menu_source(msg)

## USER VALUES ####
money_source = menu_source('\nQual o pais de origem do dinheiro?')
money_destiny = menu_source('\nQual o pais de destino do dinheiro?')
amount = menu_amount(money_from, money_to)
#
## CODES ###
from_code = money_from['code']
to_code = money_to['code']

### SCRAPING TRANFERWISE ########
tw_request = requests.get(f"{url_transfwewise}{from_code}-to-{to_code}-rate?amount={amount}", headers={'User-Agent': user_agent})
tw_soup = BeautifulSoup(tw_request.text, "html.parser")
#pega o rate para calcular
rate = float(tw_soup.find('span', class_='text-success').string)

# MATH + RESULT
rate_math = amount * rate
print(format_currency(rate_math, to_code))
format_currency(rate_math, to_code)
