
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











# url_terra = 'https://www.terra.com.br/'

# r = requests.get(url_terra)

# print(r.headers)
#
#
# Criar uma lista para guardar os dados enviados pelo usuário:
# .
#
# O programa deve tratar os erros como por exemplo:
# remover espaços vazios ao inserir a url
#
# verificar se o endereço inserido é um endereço válido ou não
# se não 'for' válido, informar “Endereço Inválido”
#
# inserir o https:// caso o usuário insira apenas o domínio
# verificar se o domínio está ON ou OFF informando o usuário por mensagem
#
# Após uma consulta, perguntar se o usuário que realizar outra ou não, dando apenas a opção dele inserir s/n ou S/N
# Se optar em não realizar outra consulta, enviar a mensagem “Programa encerrado!”
