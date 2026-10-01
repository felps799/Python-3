soma_pares = soma_terceira_coluna = maior_segunda_linha = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
print('-=-'*30)
for linha in range (0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for linha in range(0,3):
    soma_terceira_coluna += matriz[linha][2]
for coluna in range(0,3):
    if coluna == 0:
        maior_segunda_linha = matriz[1][coluna]
    elif matriz[1][coluna] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][coluna]
print('-=-'*30)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maio valor da segunda linha é {maior_segunda_linha}')