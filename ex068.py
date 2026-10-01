'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

import random
vitorias = 0
while True:
    computador = random.randint(0,11)
    jogador = int(input('Digite um Número: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o cmputador jogou {computador}. Total de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamso jogar novamente...')

print(f'Game Over! Você venceu {vitorias} vez.' if vitorias == 1 else f'Game Over! Você venceu {vitorias} vez.')