continuar = 'S'
soma = quant = media = maior = menor = 0

while continuar == "S":
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    soma += num
    quant += 1
    if quant == 1:
        maior == menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma/quant
print(f'Você digitou {quant} números e a média foi de {media}')
print(f'O menor número digitado foi {menor} e o maior foi {maior}')