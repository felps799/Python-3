'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 1
termo = primeiro_termo
while c <=10:
    print(f'{termo}', end=' →')
    termo += razao
    c +=1
    print(' ' if c<=10 else ' FIM', end='')
