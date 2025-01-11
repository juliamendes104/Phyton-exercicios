#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
print('\033[35mPrograma para converter número na base binária, octal ou hexadecimal\033[m')
numero = int(input('Digite o número a ser convertido: '))
opcao = int(input('''1.binário\n2.octal\n3.hexadecimal'''))
conversao = numero
if opcao == 1:
    conversao = bin(conversao)
elif opcao == 2:
    conversao = oct(conversao)
elif opcao == 3:
    conversao = hex(conversao)
else:
    print('Opção inválida')
print(f'Número {numero} fica convertido para {conversao[2:]}')