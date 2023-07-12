# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES. Se o valor digitado for IMPAR desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Resultado da soma entre {} números ÍMPARES: {}'.format(cont, soma))