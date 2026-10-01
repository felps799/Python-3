velocidade = float(input('Qual a velocidade do carro, em km/h? '))
if velocidade < 80:
    print('Você está dentro do limite. Dirija com cuidado!')
else:
    print ('-=-' *50)
    print(f'Você ultrapassou o limite e foi multado! \n O valor da multa é de R${(velocidade - 80) * 7:.2f}')
    print ('-=-' *50)