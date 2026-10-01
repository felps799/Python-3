num = input('Digite um número: ')
length = len(num)
if length > 4:
    print('Número inválido, digite um número de 0 a 9999')
else:
    num = num.zfill(4)
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Unidade de Milhar: {num[0]}')