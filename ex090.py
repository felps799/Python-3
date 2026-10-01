ficha = {"nome": '', "media": '', "situacao": ''}
while True:
    ficha["nome"] = str(input('Nome: '))
    ficha["media"] = float(input(f'Média de {ficha["nome"]}: '))
    if ficha["media"] < 7:
        ficha["situacao"] = 'Recuperação'
    elif ficha ["media"] <= 5:
        ficha["situacao"] = 'Reprovado'
    elif ficha ["media"] >= 7:
        ficha["situacao"] = 'Aprovado'
    break
print('-='*30)
print(f'FICHA DO ALUNO {ficha["nome"]}')
print(f'MÉDIA = {ficha["media"]}')
print(ficha["situacao"])