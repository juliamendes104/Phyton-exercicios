#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para
#salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é
#de 15%.
print('Programa para calcular o aumento')
print('-' * 50)
salario = float(input('Digite seu salário: '))
if salario > 1250.0:
    aumento = (salario * 0.1)
    print(f'O aumento será de R${aumento:.2f}, totalizando R${salario + aumento:.2f}')
else:
    aumento = salario * 0.15
    print(f'O aumento será de R${aumento:.2f}, totalizando R${aumento + salario:.2f}')