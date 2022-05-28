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
    choice_from = int(input('## -> '))
    if choice_from > len(country_all):
      print("nao tem. escolha um Nº da lista:")
    else:
      selected = country_all[choice_from]
      print(f'\n(x): {selected["name"]}\n')
      ask_country = choice_from
      money_from = selected["code"]
      menu_destiny()

  except:
    print("cara só pode numero. Tente denovo \n")
    menu_source()
    money_source = money_from

def menu_destiny():
  try:
    ## Input moeda de destino
    print("Informe agora o país de destino da moeda:\n")
    choice_to = int(input('## -> '))
    if choice_to > len(country_all):
      print("nao tem. escolha um Nº da lista:")
    else:
      selected = country_all[choice_to]
      print(f'\n(x): {selected["name"]}\n')
      ask_country = choice_to
      money_destiny = selected["code"]
      print(f'Quantos XXX você quer converter pra {money_destiny}.\n')
    ## Input valor de conversão desejado
    choice_amount = int(input('## -> '))
    ask_country = choice_amount
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

print("\nPelo número, escolha o país de origem da moeda:")

menu_source()

### USER VALUES ####
# money_source = ask_country('\n qual o pais de origem do dinheiro?')
# money_destiny = ask_country('\n qual o pais de destino do dinheiro?')
# amount = ask_amount(money_from, money_to)
#
### CODES ###
# from_code = money_source['code']
# to_code = money_destiny['code']
# from_code = money_source['code']
# to_code = money_destiny['code']
#
#### SCRAPING TRANFERWISE ########
# tw_request = requests.get(f"{url_transfwewise}{from_code}-to-{to_code}-rate?amount={amount}", headers={'User-Agent': user_agent})
# tw_soup = BeautifulSoup(tw_request.text, "html.parser")
# #pega o rate para calcular
# rate = float(tw_soup.find('span', class_='text-success').string)
#
# # MATH + RESULT
# rate_math = amount * rate
# print(format_currency(rate_math, to_code))
# format_currency(rate_math, to_code)
