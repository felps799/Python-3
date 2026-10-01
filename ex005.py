n = int(input("Digite um número: "))
a = n - 1
s = n + 1
print(f"Tendo como número {n}, o seu antecessor é {a} e o seu sucessor é {s}.")

# COMENTÁRIOS:
# adição +                            ordem de precedência: (); **; * ou / ou // ou %; + ou -
# subtração -                         na ordem em que aparecem da esquerda para a direita
# multiplicação *                     concatenar = juntar strings/variáveis
# divisão /
# potenciação ** ou pow(base, expoente)
# "raidiciação" ** (1/numero) ou pow(base, 1/numero)
# resto da divisão %                   
# comentário shift + 3                 
# divisão inteira //
# igual ==

# organizar informações 
# nome = input("Qual é o seu nome? ")
# print(f"Prazer em te conhecer {nome:=^20}!") # centralizado
# print(f"Prazer em te conhecer {nome:->20}!") # alinhado a direita
# print(f"Prazer em te conhecer {nome:-<20}!") # alinhado a esquerda
# print(f"Prazer em te conhecer {nome:-^20}!") # centralizado com traços
# print(f"Prazer em te conhecer {nome: <20}!") # espaço vazio

# operadores aritméticos
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))
# a = n1 + n2 
# s = n1 - n2
# m = n1 * n2
# d = n1/n2
# di = n1//n2
# p = n1**n2
# mo = n1%n2
# print(f"A soma é {a}, \n a subtração é {s}, \n a multiplicação é {m}, \n a divisão é {d:.3f}, \n a divisão inteira é {di}, \n a potência é {p} \n e o resto da divisão é {mo}.")