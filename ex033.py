print ('-=-' *20)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
print ('-=-' *20)

# VERIFICANDO QUEM É MENOR
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
print(f"O menor valor digitado foi {menor}")

# VERIFICANDO QUEM É MAIOR
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print(f'O maior número é {maior}')
print ('-=-' *20)

