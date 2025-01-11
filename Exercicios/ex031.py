#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 500Km e R$0,45 para viagens mais longas.
print('\nBem vindo a Santa Bárbara Airbus! Por favor selecione o destino de sua viagem: \n')
print('-' * 50)
opcao = int(input('''1. São Paulo (400KW)
2. Belo Horizonte (600KW)
3. Canarâna (1000KW)'''))
if opcao == 1:
    preco = 400 * 0.5
    print(f'Preço da passagem: R${preco:.2f}')
if opcao == 2:
    preco = 600 * 0.45
    print(f'Preço da passagem: R${preco:.2f}')
if opcao == 3:
    preco = 1000 * 0.45
    print(f'Preço da passagem: R${preco:.2f}')
print('\nAgradeçemos a preferência.')