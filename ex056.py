'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print(f'---{p}ª pessoa---')
    nome = str(input(f'Digite o nome da {p}ª pessoa: '))
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {p}ª pessoa [M/F]: ')).strip()
    media += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1


print(f'A média de idade do grupo é de {media/4} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos.')
print(f'Ao todo são {totmulher20} menores de 20 anos.')