# Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lido.
maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))