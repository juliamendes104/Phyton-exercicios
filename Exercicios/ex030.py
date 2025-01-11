#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print(f'{"Programa para calcular Impar ou Par":=^50}')
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print(f'Número {numero} é par')
else:
    print(f'Número {numero} é ímpar')