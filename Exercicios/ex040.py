#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('APROVADO')
elif media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media < 7.0:
    print('RECUPERAÇÃO')