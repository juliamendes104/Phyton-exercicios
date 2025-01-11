#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = int(input('Digite um número: '))
print(f'Dobro de {num} é {num*2}', end = '')
print(f', o triplo é {num*3}', end = ' ')
print(f'e a raiz quadrada é {num**(1/2):.2f}')