#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
print('Programa para mostrar o novo salário com aumento.')
print('-' * 60)
salario = float(input('Digite seu salário: '))
novosalario = salario + salario * 15 / 100
print(f'Novo salário: {novosalario:.2f}')