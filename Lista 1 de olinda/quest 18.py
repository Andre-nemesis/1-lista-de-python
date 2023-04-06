'''
Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.
'''
tamlist = int(input('Digite o tamanho da lista: '))
lista = []
produto = 1

for i in range(0, tamlist):
    num = int(input(f'Digite o {i + 1}º número: '))
    lista.append(num)

for i in lista:
    produto *= i

print(f'\nLista de números: {lista}\n')
print(f'Multiplicação dos números da lista: {produto}')