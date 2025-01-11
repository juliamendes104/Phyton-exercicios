#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
#dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('\nRadar da rodovia.')
velocidade = float(input('Por favor, informar a velocidade do seu veículo (em KW): '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\nLimite de velocidade ultrapassado. A multa será de R${multa:.2f}')
else:
    print('\nLimite de velocidade respeitado. Faça boa viagem.')