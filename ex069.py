'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior_idade = total_homem = mulheres_menos_vinte = 0
while True:
    print('--' * 25)
    print(f'{"CADASTRE UMA PESSOA":^50}')
    print('--' * 25)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('--' * 25)

    if idade > 18:
        maior_idade += 1
    if  sexo == 'M':
        total_homem += 1
    if sexo == 'M' and idade < 20:
        mulheres_menos_vinte += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'A quantidade de pessoas maiores de 18 anos cadastradas são{maior_idade}.')
print(f'O total de homens cadastrados são {total_homem}.')
print(f'O total de mulheres com menos de 20 anos cadastradas são {mulheres_menos_vinte}.')
