#Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m²
print('Programa para calcular quantidade de tinta necessária em litros.')
altura = float(input('Largura da parede: '))
largura = float(input('Altura da parede: '))
r = float(input('Quantos M² a lata de tinta rende? '))
l = float(input('Quantos litros tem a lata de tinta? '))
area = altura*largura
RL = r/l
print(f'Área da parede: {area:.2f} m²\nPrecisará de {area/RL:.2f} litro(s) de tinta')