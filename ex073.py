'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

times = ("Flamengo","Palmeiras","Athletico-PR","Fluminense","Bahia","Cruzeiro","Atlético-MG","Santos","Coritiba","Red Bull Bragantino","São Paulo","Botafogo","Vitória","Corinthians","Mirassol","Vasco da Gama","Grêmio","Internacional","Clube do Remo","Chapecoense")

print(f'Os cinco primeiros colocados são {times[0:6]}')
print(f'Os quatro últimos colocados são {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O time Chapecoense está na posição {times.index('Chapecoense')}ª')