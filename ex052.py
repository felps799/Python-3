numero = int(input('Digite um número: '))
tot = 0
for c in range (1, numero+1):
    if numero % c ==0:
        print(f'\033[33m {c}', end=" ")
        tot += 1
    else:
        print(f'\033[31m {c}', end=" ")

print(f'\nO número {numero} foi dividido {tot} vezes.')
if tot == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele não é primo!')