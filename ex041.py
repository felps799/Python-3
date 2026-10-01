from datetime import date
atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <=19:
    print('JÚNIOR')
elif idade <=25:
    print('SÊNIOR')
else:
    print('MASTER')