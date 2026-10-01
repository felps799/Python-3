'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

num = int(input('Digite o número: '))
c = num
f = 1
print(f'Calculando fatorial de {num}:')
while c > 0 :
    print(f'{c}', end=' ')
    print('x ' if c>1 else '=', end='')
    f = f * c
    c -=1
    

print(f' {f}')