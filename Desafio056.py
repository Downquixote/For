# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre: 
# A MÉDIA DE IDADE do grupo.
# Qual é o nome do homem MAIS VELHO.
# Quantas mulheres têm MENOS DE 20 anos.
somaIdade = 0
m = 0
homemIdade = 0
nomeVelho = ''
idadeMulher = 0

for p in range(1, 5):
    nome = str(input('Nome da {}º pessoa: '.format(p))).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    print('='*20)
    
    if p == 1 and sexo in 'M':
        homemIdade = idade
        nomeVelho = nome
    if sexo in 'M' and idade > homemIdade:
        nomeVelho = nome
    if sexo in 'F' and idade < 20:
        idadeMulher += 1

m = somaIdade / 4
print('A média de idade do grupo é de {} anos de idade.'.format(m))
print('O homem mais velho têm {} anos de idade e se chama: {}'.format(homemIdade, nomeVelho))
print('Total de {} mulheres têm menos de 20 anos.'.format(idadeMulher))