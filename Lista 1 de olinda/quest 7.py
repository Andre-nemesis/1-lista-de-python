'''
Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa.
'''
nomes = []
numpalavra = int(input('Quantidade de nomes: '))

print('Digite os nomes: ')

for i in range(0,numpalavra):
    palavra = (str(input(f'Digite a {i + 1}º palavra: ')))
    nomes.append(palavra)
    maiorpalavra = max(nomes,key=len)

print(f'Essa foi a maior palavra: "{maiorpalavra}"')