time = list()
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador["Nome"] = str(input('Nome do Jogador: '))
    total_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    total_gols = 0
    partidas.clear()
    for c in range(0,total_partidas):
        partidas.append(int(input(f'    Quantos gols na {c+1}ª partida? ')))
        total_gols += partidas[c]
    jogador["Gols"] = partidas.copy()
    jogador["Total de Partidas"] = total_partidas
    jogador["Total de Gols"] = total_gols
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in "SN":
            break
        print('Erro! Digite apenas S ou N')
    if resposta == 'N':
        break

print('-='*40)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-_'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')

