from time import sleep
import random 
numero = random.randint(0, 5)
print ('-=-' *50)
chute = int(input('Digite um número entre 0 e 5: '))
print ('-=-' *50)
print ('PROCESSANDO...')
sleep(3)
if chute == numero:
    print('Parabéns! Você pensou no número certo!')
else:
    print(f'Você errou! O número que pensei foi {numero} e não {chute}')