#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da
#casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
#do salário ou então o empréstimo será negado.
print('\033[35mPrograma para aprovar o empréstimo bancário para a compra de uma casa:\033[m')
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = float(input('Digite em quantos anos o comprador vai pagar: '))
prestacao = casa / (anos * 12)
if prestacao > (salario * 0.3):
    print('Empréstimo negado.')
else:
    print(f'Empréstimo aprovado com prestação no valor de R${prestacao:.2f}')