'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite o sexo [M/F]: ')).upper()
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Opção incoerente! Digite novamente o sexo [M/F]: '))