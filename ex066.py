'''break = interromper laço infinito (while true) dentro de um if identado no while true'''
cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Você digitou {cont} números e a soma entre eles é de {soma}')