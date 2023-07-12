# Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year
totalMenor = 0
totalMaior = 0
for pessoa in range(1, 8):
    nasci = int(input('Digite o ano de nascimento da {}º pessoa: '.format(pessoa)))
    ano = atual - nasci
    if ano < 18:
        totalMenor += 1
    else:
        totalMaior += 1
print('Total de {} pessoas maiores de idade!'.format(totalMaior))
print('Total de {} pessoas menores de idade! '.format(totalMenor))