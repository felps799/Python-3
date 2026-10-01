valores = [int(input('Digite o primeiro valor: ')), 
           int(input('Digite o segundo valor: ')), 
           int(input('Digite o terceiro valor: ')), 
           int(input('Digite o quarto valor: ')), 
           int(input('Digite o quinto valor: '))]
print('-='*50)

menor = maior = cont = 0
for numero in valores:
    if cont == 0:
        menor = maior = numero
        cont += 1
    else:
        if menor > numero:
            menor = numero
        if maior < numero:
            maior = numero

print(f'Os valores que você digitou foi {valores}')
print(f'O maior valor digitado foi {maior} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {menor} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')