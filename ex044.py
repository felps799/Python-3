print('='*20 + 'CASA DE PERFUMES' + '='*20)
preco = float(input('Digite o valor da compra: R$'))
print('''Escolha a forma de pagamento:
[1]DINHEIRO
[2]CARTÃO À VISTA
[3]CARTÃO EM DUAS VEZES
[4]CARTÃO ACIMA DE TRÊS VEZES''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'Você pagará R${(preco - 0.1*preco):.2f}')
elif escolha == 2:
    print(f'Você pagará R${(preco - 0.05*preco):.2f}')
elif escolha == 3:
    print(f'Você pagará R${preco}')
elif escolha == 4:
    print(f'Você pagará R${(preco + 0.2*preco):.2f}')
else:
    print('OPÇÃO INVÁLIDA!')