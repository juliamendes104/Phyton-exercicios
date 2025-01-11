# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print('-' * 50)
h = int(input('Informe o horário. Horas:'))
m = int(input('Minutos:'))
c = float(input('Informe a temperatura em graus Celsius:'))
f = 1.8 * c + 32
print('-' * 50)
print(f'Time: {h}:{m} Degrees Fahrenheit: {f}ºF')