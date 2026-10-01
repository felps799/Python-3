print ('-=-' *50)
ano = int(input("Digite o ano que você quer analisar: "))
print ('-=-' *50)
if ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano de {ano} é BISSEXTO!")
else:
    print(f"O ano de {ano} NÃO É BISSEXTO!")
print ('-=-' *50)