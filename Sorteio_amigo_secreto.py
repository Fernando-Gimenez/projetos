import random


# lista de pessoas da familia
lista = ['fernando', 'juliana', 'alice', 'rebeca', 'dona_cida', 'vovo_murilo', 'patricia', 'artur', 'lorenzo', 'miguel', 'renata', 'diego', 'murilinho', 'ester']

# funcao para embaralhar os nomes da lista
random.shuffle(lista)


print('resultado_sorteio :')
for i in range(len(lista)):
    amigo_secreto = lista[(i + 1) % len(lista)]
    print(lista[i], 'tirou', amigo_secreto)
    

























