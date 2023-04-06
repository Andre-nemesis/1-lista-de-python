'''
Crie um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares.
'''
tamlist = int(input('Digite o tamanho da lista: '))
lista = []
impar = []

for i in range(0, tamlist):
    num = int(input(f'Digite o {i + 1}º número: '))
    lista.append(num)

    if num % 2 != 0:
        impar.append(num)

print(f'Lista de números: {lista}\n')
print(f'Números ímpares da lista {impar}\n\nSoma dos números ímpares da lista: {sum(impar)}')