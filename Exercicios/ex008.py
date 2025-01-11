#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
num = float(input('Digite um número em metros: '))
print(f'{num:.2f} metros:\n{num*100:.0f} centímetros\n{num*1000:.0f} milímetros')