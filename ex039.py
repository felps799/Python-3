from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano}, hoje em {atual}, tem {idade}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    falta = 18 - idade
    print(f'Você ainda não tem idade para se alistar. Ainda restam {falta} anos.')
    futuro = falta + atual
    print(f'Você se alistará em {futuro}')

else:
    sobra = idade - 18
    print(f'Você está atrasado para se alistar há {sobra} ano(s).')
    passado = atual - sobra
    print(f'Você deveria ter se alistado em {passado}')