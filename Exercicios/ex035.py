#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
#formar um triângulo.
print(f'{"Programa pra verificar se três retas podem formar um triângulo":=^100}')
reta1 = int(input('Digite o comprimento da primeira reta: '))
reta2 = int(input('Digite o comprimento da segunda reta: '))
reta3 = int(input('Digite o comprimento da terceira reta: '))
if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print(f'As restas de comprimento {reta1}, {reta2} e {reta3} podem formar um triângulo')
else:
    print('Não podem formar um triângulo')