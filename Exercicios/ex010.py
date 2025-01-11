#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
num = float(input('Quanto dinheiro tem na carteira? R$'))
#print(f'Com {num:.2f}, pode comprar US${num//3.27} dólares e restará R${num%3.27:.2f} na carteira')
print(f'Com R${num:.2f}, pode comprar US${num/3.27:.2f}')