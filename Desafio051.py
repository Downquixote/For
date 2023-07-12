# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (11 - 1) * r
for c in range(a1, decimo, r):
    print('{}'.format(c), end=' - ')
print('ACABOU!')