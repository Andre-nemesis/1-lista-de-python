'''
Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.
'''
num = float(input('Digite um número para saber se ele é par ou ímpar: '))

if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))