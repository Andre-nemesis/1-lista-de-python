'''
Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".
'''
tamlist = int(input('Digite o tamanho da lista de palavras: '))
palavras = []
palavrascoma = []
for i in range(0,tamlist):
    palavr = str(input(f'Digite a {i + 1}º palavra: '))
    palavras.append(palavr)

    if palavr[0] == 'a' or palavr[0] == 'A':
        palavrascoma.append(palavr)

print(f'Palavras da lista: {palavras}')
print(f'Palavras que começam a letra "a": {palavrascoma}')