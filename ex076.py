'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print('=='*25)
print(f"{'Listagem de Preços':^50}")
print('=='*25)
produtos = ("Lápis", 2.50, 
            "Caderno", 15.00, 
            "Borracha", 1.75, 
            "Caneta", 3.00, 
            "Mochila", 85.00)

for posicao in range (0, len(produtos)):
    if posicao %2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')
    else:
        print(f'R${produtos[posicao]:>5.2f}')
print('=='*25)
