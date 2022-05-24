import requests
from bs4 import BeautifulSoup

url = 'https://www.iban.com/currency-codes'
r_iban = requests.get(url)
html_doc = r_iban.text

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
            'name': country,
            'code': currency
        }
        country_all.append(info_country)


# print(country_all)

def menu():
  try:
    choice = int(input("## -> "))
    if choice > len(country_all):
      print("nao tem. escolha da lista:")
    else:
      selected = country_all[choice]
      print(country)
      print(f"O pais que vc escolheu: {selected['name']} \n e a moeda é {selected['code']}")
      print("escolha outro pais: \n")
      menu()
  except:
    print("cara só pode numero. Tente denovo \n")
    menu()


print("Bem-vindo! \n Escolha o pais quer consultar pelo numero\n")

for index, info_country in enumerate(country_all):
  print(f"{index} - {info_country['name']}")

print("escolha o pais:")

menu()
