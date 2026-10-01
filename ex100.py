from random import randint

def sortear_somar(quantia_numeros):
    numeros = []
    soma_par = 0
    while len(numeros) < quantia_numeros:
        numeros.append(randint(inicio,fim))
    print(f'Sorteando {quantia_numeros} valores.')
    print(f'Somando os valores pares de {numeros}', end='')
    for numero in numeros:
        if numero %2 == 0:
            soma_par += numero
    print(f' temos {soma_par}.')
    

inicio = int(input('De onde deseja iniciar o range? '))
fim = int(input('Onde deseja finalizar o range? '))
quantia_numeros = int(input('Quantos números deseja sortear? '))
sortear_somar(quantia_numeros)