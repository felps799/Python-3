import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input('''Considere:
1 = PEDRA
2 = PAPEL
3 = TESOURA
Agora, digite sua escolha: '''))
b = random.randint(1,3)
print (b)
if a > 3 and a < 1:
    print('OPÇÃO INVÁLIDA!')
elif a == b:
    print ("EMPATE")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")