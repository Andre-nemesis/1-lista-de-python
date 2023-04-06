'''
Crie um programa que leia um número do usuário e exiba a sua raiz quadrada
'''
import math

num = float(input('Digite um número para realizar seu cálculo de raiz: '))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é {}'.format(num,raiz))