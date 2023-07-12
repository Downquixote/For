# Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo entre 1 e 50

num = int(input('Digite um número até 50 para ver seus antessessores pares: '))
if num <= 50:
    for c in range(0, num, 2):
        print(c)
    print('===== FIM =====')
else: 
    print('Opção inválida!')