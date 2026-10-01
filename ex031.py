distancia = float(input("Qual a distância da sua viagem? "))
if distancia <=200:
    print(f'O custo da sua viagem será de {distancia * 0.50}')
else:
    print(f'O custo da sua viagem será de {distancia * 0.45}')