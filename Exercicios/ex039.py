#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele
#ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
#alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - ano_nascimento
if idade > 18:
    print(f'Já passou do tempo de alistamento em {idade-18} ano(s)')
elif idade < 18:
    print(f'Vai se alistar daqui {18-idade} ano(s)')
else:
    print('É a hora exata de se alistar')