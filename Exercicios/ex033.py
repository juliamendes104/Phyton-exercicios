#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Programa para descobrir o maior e o menor número: ')
print('-' * 50)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
#maior = 0
#menor = 0
if num1 > num2:
    if num1 > num3:
        maior = num1
        if num2 > num3:
            menor = num3
        else:
            menor = num2
    else:
        maior = num3
        menor = num2
else:
    if num2 > num3:
        maior = num2
        if num3 > num1:
            menor = num1
        else:
            menor = num3
    else:
        maior = num3
        menor = num1
print(f'O maior número é o {maior} e o menor é o {menor}')