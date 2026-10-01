pessoa = dict()
galera = list()
soma = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input('Nome: '))
    while True:
        pessoa["Sexo"] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa["Sexo"] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F')
    pessoa["Idade"] = int(input('Idade: '))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if resposta == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média das idades das pessoas cadastradas é {soma/len(galera):.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p["Sexo"] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print(f'D) Lista das pessoas com idade acima da média: ')
for p in galera:
    if p['Idade'] >= (soma/len(galera)):
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')