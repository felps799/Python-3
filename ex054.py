from datetime import date
maiores = 0
menores = 0
hoje = date.today().year
for i in range (1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if hoje - ano >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Nesse grupo tem {maiores} pessoas maiores de idade e {menores} pessoas menores de idade')