'''
Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.
'''
tamlist = int(input('Digite o tamanho da lista: '))
listanum = []
nummaior10 = []

for i in range(0,tamlist):
    numeros = float(input(f'Digite o {i + 1}º número: '))
    listanum.append(numeros)

    if numeros > 10:
        nummaior10.append(numeros)

print(f'Lista de números: {listanum}')
print(f'Números maiores que 10 na lista: {nummaior10}')