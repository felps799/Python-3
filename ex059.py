'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print('--=--' *20)
print('Escolha o que deseja fazer:')
print('[ 1 ] somar \n' 
    '[ 2 ] multiplicar \n'
    '[ 3 ] maior \n'
    '[ 4 ] novos números \n'
    '[ 5 ] sair do programa')
escolha = 0
while escolha != 5:
    escolha = int(input('O que deseja fazer? '))
    if escolha == 1:
        print(f'A soma entre {n1} e {n2} vale {n1+n2}.')

    elif escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} vale {n1*n2}.')

    elif escolha == 3:
        if n1 > n2:
            print(f' {n1} é maior do que {n2}')
        elif n1 == n2:
            print(f' {n1} é igual a {n2}')
        else:
            print(f' {n2} é maior do que {n1}')

    elif escolha == 4:
        n1 = float(input('Digite novamente o primeiro valor: '))
        n2 = float(input('Digite novamente o segundo valor: '))

    elif escolha == 5:
        print('Tchau!')
        break

    else:
        print('Opção inválida. Tente novamente')