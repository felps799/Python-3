numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado!')

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
    if continuar not in 'Ss':
        continuar = str(input('Quer continuar? [S/N] '))

print('-='*50)
numeros.sort()
print(f'Você digitou os valores {numeros}')