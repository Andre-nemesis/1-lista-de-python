'''
Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.
'''
tamlist = int(input('Digite o tamanho da lista: '))
listanum = []

for i in range(0,tamlist):
    numero = int(input(f'Digite o {i+1} número: '))
    listanum.append(numero)

maiornum = max(listanum)

print(f'Lista de números: {listanum}')
print(f'Esse é o maior número da lista: {maiornum}')