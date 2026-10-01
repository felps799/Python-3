jogador = {}
partidas = []
jogador["Nome"] = str(input('Nome do Jogador: '))
total_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
total_gols = 0
for c in range(0,total_partidas):
    partidas.append(int(input(f'    Quantos gols na {c+1}ª partida? ')))
    total_gols += partidas[c]
    
jogador["Total de Partidas"] = total_partidas
jogador["Total de Gols"] = total_gols
print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O {jogador["Nome"]} jogou {jogador["Total de Partidas"]} partidas.')
for p in range(0, total_partidas):
    print(f'    => Na partida {p}, fez {partidas[p]} gols.')
print(f'Foi um total de {total_gols} gols.')