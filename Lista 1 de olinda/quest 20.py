'''
Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente.
'''
tamlist = int(input('Digite o tamanho da lista: '))
lista = []

for i in range(0, tamlist):
    num = int(input(f'Digite o {i + 1}º número: '))
    lista.append(num)

print(f'\nLista de números: {lista}\n')
print(f'Números da lista ordenados de forma decresente: {sorted(lista,reverse=True)}')