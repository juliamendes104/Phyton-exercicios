#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
from math import sqrt
print('Programa para calcular a hipotenusa de um triângulo retângulo')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt(co ** 2 + ca **2)
print(f'Cateto oposto: {co}\nCateto adjacente: {ca}\nHipotenusa: {h:.1f}')