#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc, floor
enter = input('Programa para mostrar a porção inteira de um número real. Pressione ENTER')
num = float(input('Digite um número real: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')