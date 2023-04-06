'''
Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.
'''
tamlist = int(input('Digite o tamanho da lista: '))
listanum = []

for i in range(0,tamlist):
    numero = int(input(f'Digite o {i+1} número: '))
    listanum.append(numero)

for i in listanum:
    numsoma = sum(listanum)

print(f'Lista de números: {listanum}')
print(f'Esse foi o resultado da soma da lista: {numsoma}')