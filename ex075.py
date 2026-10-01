'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input('Digite o primeiro número: ')),
          int(input('Digite o segundo número: ')),
          int(input('Digite o terceiro número: ')),
          int(input('Digite o quarto número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.' if 9 in numeros else 'O valor 9 não foi digitado!')
print(f'O valor 3 apareceu, primeiramente, na posição {numeros.index(3)+1}' if 3 in numeros else 'O número 3 não foi digitado!')
print('Os valores pares digitados foram: ')
for num in numeros:
    if num %2 == 0:
        print(num, end=" ")