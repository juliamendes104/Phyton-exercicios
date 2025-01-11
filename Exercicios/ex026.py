#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que 
#posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase qualquer: ')).strip()
recorrencia = frase.lower().count('a')
primeira = frase.lower().find('a')
#invertida = frase[::-1]
#ultima = (len(frase) - 1) - (invertida.lower().find('a'))
ultima = frase.lower().rfind('a')
print(f'A frase "{frase}" possui {recorrencia} vezes a letra A\nEla aparece primeiro na posição {primeira}\nEla aparece por último na posição {ultima}')