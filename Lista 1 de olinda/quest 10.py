'''
Crie um programa que leia uma lista de números do usuário e exiba a média desses números.
'''
tamlist = int(input('Digite o tamanho da lista: '))
listanum = []

for i in range(0,tamlist):
    numero = int(input(f'Digite o {i+1} número: '))
    listanum.append(numero)

media = sum(listanum) / tamlist

print(f'Lista de números: {listanum}')
print(f'Essa é a média da lista: {media}')