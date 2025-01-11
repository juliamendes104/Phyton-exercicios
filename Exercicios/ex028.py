#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na
#tela se o usuário venceu ou perdeu.
import random
numero = random.randint(0,5)
print(f'{"Bem vindo, usuário!":=^50}\nEu pensei em um número entre 0 e 5.')
resposta = str(input('Será que você é capaz de advinhar? S ou N?'))
if resposta == 'S':
    palpite = int(input('Gosto de um desafiante. Em que número pensei? '))
    if palpite == numero:
        print('Correto! Parabéns, você advinhou.')
    else:
        print(f'Não foi dessa vez. O número que pensei era {numero}')
else:
    print('Talvez em uma próxima...')
