#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
#ângulo.
from math import cos, sin, tan
print('Programa que calcula o seno, cosseno e tangente de um número')
angulo = float(input('Digite um ângulo: '))
radiano = angulo * (3.14/180)
s = sin(radiano)
c = cos(radiano)
t = tan(radiano)
print(f'Dado o ângulo {angulo:.0f}°, seu seno é {s:.2f}, seu cosseno é {c:.2f} e sua tangente é {t:.2f}')