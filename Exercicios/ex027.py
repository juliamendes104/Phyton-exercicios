#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
#nome separadamente.
nome = str(input('Digite seu nome completo: '))
lista = nome.split()
indice = len(lista) - 1
print(f'Primeiro nome: {lista[0]}\nÚltimo nome: {lista[indice]}')