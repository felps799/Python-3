n = int(input("Digite um número: "))
i = int(input("Digite um número para calcular a raiz: "))
d = n*2
t = n*3
r = n**(1/i)
print(f"Tendo como número {n}, seu dobro é {d}, seu triplo é {t} e sua raiz {i}ª é {r:.2f}.")

#  o :.2f significa que o resultado será exibido com duas casas decimais.
#   alternativa mais curta
# n = int(input("Digite um número: "))
# i = int(input("Digite um número para calcular a raiz: "))
# print(f"Tendo como número {n}, seu dobro é {n*2}, seu triplo é {n*3} e sua raiz {i}ª é {n**(1/i):.2f}.")