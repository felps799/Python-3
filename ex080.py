lista = []
for c in range (0,5):
    n = int(input('Digite um Valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            lista.insert(pos, n)
            print(f'Adicionado na posição {pos} da lista.')
            break
        pos += 1
print('-=-'*30)
print(f'Os vaores digitados em ordem foram {lista}')