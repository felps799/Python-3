'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

print("--=--" *20)
print("A PA que você descreveu tem os seguintes elementos:")
print(a1)
for i in range (2,11):
    print(a1 + (i-1)*r)
print("--=--" *20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1)*razao
for c in range (primeiro, decimo+razao, razao):
    print(c, end="; ")