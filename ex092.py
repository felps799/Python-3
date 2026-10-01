from datetime import date
ficha = {
    "nome": '',
    "idade": '',
    "ct": '',
    "ano contratação": '',
    "salário": ''}

while True:
    print('-='*30)
    ficha["nome"] = str(input('Nome: '))
    ficha['idade'] = date.today().year - int(input('Data de Nascimento: '))
    ficha['ct'] = int(input('Número da Carteira de Trabalho: '))
    if ficha['ct'] == 0:
        print(f'=== CADASTRO DE TRABALHO {ficha["nome"]} ===')
        print(f'Idade: {ficha["idade"]}')
        print(f'Sem Carteira de Trabalho')
    else:
        ficha['ano contratação'] = int(input('Ano de Contratação: '))
        ficha['salário'] = float(input('Salário: '))

        print(f'=== CADASTRO DE TRABALHO {ficha["nome"]} ===')
        print(f'Idade: {ficha["idade"]}')
        print(f'Carteira de Trabalho N° {ficha["ct"]}')
        print(f'Ano de Contratação: {ficha["ano contratação"]}')
        print(f'Salário: R${ficha["salário"]}')
        print(f'Ano de Aposentadoria: {ficha["ano contratação"] + 35}')
    break