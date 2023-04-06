'''
Crie um programa que leia uma lista de números do usuário e exiba somente os números pares.
'''
tamlist = int(input('Digite o tamanho da lista: '))
listanum = []
par = []

for i in range(0,tamlist):
    numero = int(input(f'Digite o {i+1} número: '))
    listanum.append(numero)
    if numero % 2 == 0:
        par.append(numero)
        
print(f'Lista de números: {listanum}')
print(f'Números pares da lista: {par}')