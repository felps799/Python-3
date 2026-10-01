r1 = float(input("Digite o tamanho da reta 1: "))
r2 = float(input("Digite o tamanho da reta 2: "))
r3 = float(input("Digite o tamanho da reta 3: "))

if r1+r2>r3 and r2+r3>r1 and r3+r2>r1:
    print ('As retas podem formar um triângulo')
    if r1==r2==r3:
        print('É um triângulo equilátero')
    elif r1==r2 or r1==r3 or r2==r3:
        print('É um triângulo isósceles')
    else:
        print('É um triângulo escaleno')
else:
    print('As retas não podem formar um triângulo')