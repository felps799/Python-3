def calcular_area():
    print("--"*30)
    l = float(input('Digite a largura, em metros: '))
    c = float(input('Digite o comprimento, em metros: '))
    print("--"*30)
    print('CALCULANDO ÁREA...')
    area = l*c
    print(f'A área de um terreno de {l}m de largura e {c}m de comprimentos é igual a {area}m².')

calcular_area()