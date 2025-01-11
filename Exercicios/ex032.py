#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print('Programa para saber se o ano é bissexto')
print('-' * 50)
ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
resposta = input('\nVocê deseja saber qual vai ser o próximo ano bissexto? S ou N?')
if resposta == 'S':
    if (ano + 1) % 4 == 0:
        print(f'O próximo ano bissexto será: {ano + 1}')
    elif (ano + 2) % 4 == 0:
        print(f'O próximo ano bissexto será: {ano + 2}')
    elif (ano + 3) % 4 == 0:
        print(f'O próximo ano bissexto será: {ano + 3}')
    else:
        print(f'O próximo ano bissexto será: {ano + 4}')
else:
    print('Okay')