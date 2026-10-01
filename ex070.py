'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total_gasto = produtos_cem = menor = cont = 0
produto_barato = ' '
nome_barato = ' '

while True:
    print('--' * 25)
    print(f'{"CASA DE PERFUMES":^50}')
    print('--' * 25)

    nome_produto = ' '
    while nome_produto == ' ':
        nome_produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$'))

    cont += 1
    total += preco
    if preco > 1000:
        produtos_cem += 1
    if cont == 1:
        menor == preco
        nome_barato = nome_produto
    else:
        if preco < menor:
            menor = preco
            nome_barato = nome_produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total gasto nessa compra foi de R${total}.')
print(f'A quantia de produtos comprados que custam mais que R$1000 é de {produtos_cem}.')
print(f'O produto mais barato nessa compra é o {nome_barato} e custa de R${produto_barato}.')