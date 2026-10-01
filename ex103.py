# def ficha(nome='', gols=0):
#     ficha = {
#         "Nome": nome,
#         "Gols": gols}
#     return ficha

# dados = ficha('Marcio',7)
# for chave, valor in dados.items():
#     print(f'{chave:<10}{valor:>5}')

def ficha(jogador='<desconhecido>', gol = 0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)