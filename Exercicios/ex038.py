#Escreva um programa que leia dois números inteiros e compare-os
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
else:
    print('Os dois são iguais')