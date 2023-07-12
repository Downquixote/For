# Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.
# Ex: APOS A SOPA (mesma palavra de trás para frente.)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('Resultado: {} - {}'.format(junto, inverso))
    print('Sua palavra é palíndroma!')
else:
    print('Resultado: {} - {}'.format(junto, inverso))
    print('Sua palavra não é palíndroma!')