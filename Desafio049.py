# Refaça o DESAFIO009, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um laço FOR.

num = int(input('Digite um número: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num*c))