# Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma dos {} valores divisiveis por 3 deu: {}'.format(cont, soma))
