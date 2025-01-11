#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = str(input('Digite um número de 0 a 9999: '))
aux = '0000' + numero
indice = len(numero)
resultado = aux[indice:]
print(f'Unidade: {resultado[3]}\nDezena: {resultado[2]}\nCentena: {resultado[1]}\nMilhar: {resultado[0]}')

numero = int(input('Digite um número de 0 a 9999: '))
milhar = numero // 1000
c = numero % 1000
centena = c // 100
d = c % 100
dezena = d // 10
unidade = d % 10
print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')