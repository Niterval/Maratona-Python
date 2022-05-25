import requests
from bs4 import BeautifulSoup
# from babel.numbers import format_currency


header = {'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

url_iban = 'https://www.iban.com/currency-codes'
url_wise = 'https://wise.com/gb/currency-converter/'
r_iban = requests.get(url_iban)
html_doc = r_iban.text


def menu_source():
  try:
    ## Input moeda de origem
    choice = int(input('## -> '))
    if choice > len(country_all):
      print("nao tem. escolha um Nº da lista:")
    else:
      selected = country_all[choice]
      print(f'\n(x): {selected["name"]}\n')
      menu_destiny()

  except:
    print("cara só pode numero. Tente denovo \n")
    menu_source()

def menu_destiny():
  try:
    ## Input moeda de destino
    print("Informe agora o país de destino da moeda:\n")
    choice = int(input('## -> '))
    if choice > len(country_all):
      print("nao tem. escolha um Nº da lista:")
    else:
      selected = country_all[choice]
      print(f'\n(x): {selected["name"]}\n')
      print(f'Quantos XXX você quer converter pra {selected["code"]}.\n')
    ## Input valor de conversão desejado
    choice = int(input('## -> '))
      # menu_destiny()
      # print("Informe agora o país de destino da moeda:\n")

  except:
    print("cara só pode numero. Tente denovo \n")
    menu_destiny()


## ## SCRAPE IBAN #######
soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')[1:]

country_all = []

for row in rows:
    items = row.find_all('td')
    country = items[0].text
    currency = items[2].text

    if currency != '':

        info_country = {
            'name': country.capitalize(),
            'code': currency
        }
        country_all.append(info_country)



print("BEM-VINDO(a)! Escolha pelo número os dois paises\nque você deseja negociar as moeda\n")

for index, info_country in enumerate(country_all):
  print(f"{index} - {info_country['name']}")

print("\nPelo número, escolha o país de origem da moeda:")

menu_source()
