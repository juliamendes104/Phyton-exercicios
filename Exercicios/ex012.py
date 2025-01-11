#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
print('Programa para mostrar o novo preço de um produto com desconto.')
print('-' * 60)
preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o desconto em porcentagem: '))
novopreco =  preco - preco*desconto/100
print(f'Novo preço: R${novopreco:.2f}')