def escreva():
    frase = str(input('Qual frase quer escrever? '))
    tamanho = len(frase) + 10
    print('-'*tamanho)
    print(f'{frase:^{tamanho}}')
    print('-'*tamanho)

escreva()