from time import sleep
def maior(*numeros):
    print('-='*20)
    maior = cont = 0
    print('Analisando os valores passados...')
    sleep(1)
    for numero in numeros:
        print(f'{numero}', end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    for numero in numeros:
        if cont == 0:
            maior = numero
            cont += 1
        if numero > maior:
            maior = numero
    print(f'O maior valor informado foi {maior}.')

maior(2,3,4,5,17,20,100,9,6,5)