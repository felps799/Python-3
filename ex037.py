print('--=--' *20)
numero = int(input('Digite o número: '))
print('''Escolha a base de conversão:
[1]Converter para BINÁRIO 
[2]Converter para HEXADECIMAL
[3]Converter para OCTADECIMAL''')
escolha = int(input('Sua opção: '))
print('--=--' *20)

if escolha == 1:
    print(f'O número {numero} convertido para BINÁRIO equivale a {bin(numero)}')
elif escolha == 2:
    print(f'O número {numero} convertido para HEXADECIMAL equivale a {hex(numero)}')
elif escolha == 3:
    print(f'O número {numero} convertido para BINÁRIO equivale a {oct(numero)}')
else: 
    print('\033[1;41m Opção Inválida \033[m')
print('--=--' *20)