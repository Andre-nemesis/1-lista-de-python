'''
Crie um programa que leia uma lista de números do usuário e exiba a soma dos números pares.
'''
tamlist = int(input('Digite o tamanho da lista: '))
lista = []
par = []

for i in range(0, tamlist):
    num = int(input(f'Digite o {i + 1}º número: '))
    lista.append(num)

    if num % 2 == 0:
        par.append(num)

print(f'Lista de números: {lista}\n')
print(f'Números pares da lista {par}\n\nSoma dos números pares da lista: {sum(par)}')