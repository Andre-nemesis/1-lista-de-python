'''
Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.
'''
tamlist = int(input('Digite o tamanho da lista: '))
listanum = []
nummenor5 = []

for i in range(0,tamlist):
    numeros = float(input(f'Digite o {i + 1}º número: '))
    listanum.append(numeros)

    if numeros < 5:
        nummenor5.append(numeros)

print(f'Lista de números: {listanum}')
print(f'Números menores que 5 na lista: {nummenor5}')