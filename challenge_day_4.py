
import requests
import os

def link_system():
    print('Bem vindo ao verificador de sites 1.0!')
    print('Insira as Url´s separadas por vírgula dos sites que desja verificar o status.\n')

    urls = input().lower().split(",")

    for link in urls:
        link = link.strip()

        if '.' not in link:
            print('Url Invalida')
        else:
            if 'https' not in link:
                link = f'https://{link}'
            try:
                r = requests.get(link)
                if r.status_code == 200:
                    print('Site online!')
                else:
                    print(f'[{link} Site onffiline]')
            except:
                print(f'{link} tente mais tarde!')
                menu()
            print('----------------\n')
            menu()

def menu():
  print("precisa verificar mais algum site? (s/n)")
  choice = input().lower()

  if choice == "s" or choice =="n":
    if choice == "n":
      print("encerrado! obrigado")
    else:
      os.system('clear')
      link_system()
  else:
    print("valor invalido")
    menu()

link_system()
