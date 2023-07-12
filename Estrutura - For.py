# Para imprimir várias vezes na tela.
for a in range(0, 5):
    print('Olá')
print('FIM')
print('='*20)

# Para contar até o número desejado.
for b in range(0, 11):
    print(b)
print('FIM')
print('='*20)

# Para contagem regressiva.
for c in range(10, 0, -1):
    print(c)
print('FIM')
print('='*20)

# Para pular números
for d in range(0, 11, 2):
    print(d)
print('FIM')
print('='*20)

# Exemplo
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')
print('='*20)

# Somatório
s = 0 
for c in range(0, 5):
    n = int(input('Digite um número: '))
    s += n
print('A soma de todos os valores: {}'.format(s))