print('Auxiliar os exercícios e manter para estudo')


def add_food(food_name='', description=''):
    if food_name != str(food_name) or description != str(description):
            print ('Não é permitido número aqui, apenas texto.')

    elif food_name =='' or description == '':
            print ('Vcoẽ precisa informar nome da comida + descrição.')

    elif food_name in food_list:
        print(f'{food_name} já está cadastrado na lista')

    else:
        return print(f'{food_name} cadastrado com sucesso!')




#
# # ADD_FOOD - TESTE 2
# print("\n#### ADD_FOOD - TESTE 2")
# print("Usando add_food sem passar a descrição.")
# print("add_food('pizza')\n")
# #excuta:
# add_food('pizza')
