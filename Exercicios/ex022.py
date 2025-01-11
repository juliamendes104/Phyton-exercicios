#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
nome_lista = nome.split()
print('-' * 50)
print(f'''Seja bem vindo(a) {nome}!\nCom letras maiúsculas: {nome.upper()}\nCom letras minúsculas: {nome.lower()}
Seu nome tem {len(''.join(nome_lista))} letras ao total\nSeu primeiro nome tem {len(nome_lista[0])} letras''')