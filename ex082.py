valores = []
valores_pares = []
valores_impares = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num %2 == 0:
        valores_pares.append(num)
    else:
        valores_impares.append(num)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('-=-'*30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {valores_pares}')
print(f'A lista de ímpares é {valores_impares}')