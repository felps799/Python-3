lista_um = []
lista_dois = []
while True:
    lista_um.append(str(input('Nome: ')))
    lista_um.append(str(input('Peso: ')))
    lista_dois.append(lista_um[:])
    lista_um.clear()
    continuar = str(input('Deseja Continuar? '))
    if continuar in 'Nn':
        break
print(lista_dois)