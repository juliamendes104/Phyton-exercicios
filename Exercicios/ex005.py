#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
num = int(input('Digite um número:'))
print(f'O antecessor de {num} é {num-1}', end = ' ')
print(f'e o sucessor de {num} é {num+1}')