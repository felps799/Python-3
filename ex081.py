valores = []
valor_5 = False
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num == 5:
        valor_5 = True
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} números')
print(f'A lista dos valores digitados em ordem decrescente é {valores}')
if valor_5 == True:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')