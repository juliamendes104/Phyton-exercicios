#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Digite o nome da cidade: ')).strip()
print(f'A cidade {cidade} começa com Santo? {cidade.lower().find("santo")==0}')