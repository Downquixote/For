# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício.
# Indo de 10 ATÉ 0, com uma pausa de 1 SEGUNDO entre eles.

from time import sleep

print('Contagem regressiva!')
print('='*20)

user = int(input('Digite o número 0 para iniciar: '))
if user == 0:
    for c in range(10, 0, -1):
        print(c)
        sleep(1)
    print('KABUMMMMMMM!')
else: 
    print('Opção inválida!')