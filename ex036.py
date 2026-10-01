# CORES NO TERMINAL
# \033[style;text;backm
# style: 
# 0 - none;   4 - underline; 
# 1 - bold;   7 - negative;

# text: 
# 30 - white;   34 - blue;
# 31 - red;     35 - purple; 
# 32 - green;   36 - ciano;
# 33 - yellow;  37 - gray;

# back: 
# 40 - white;    44 - blue;
# 41 - red;      45 - purple;
# 42 - green;    46 - ciano;
# 43 - yellow;   47 - gray;

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# Regras:
# 1- Para pedir o emprestimo você deve ter todos os dados a seguir (Nome Completo, Idade, CPF, renda)
# 2- renda minima de 1500 para revisão humana, de 1500-5000 automatizada, abaixo de 1500 está bloqueado
# 3- 1 a 20 mil automatizado, de 20.001 até 50 mil revisão humana, acima de 50 mil bloqueado
# 4- somente acima de 18 anos

from time import sleep
print('--=--' *20)
nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
cpf = str(input('Digite seu CPF: '))
renda = float(input('Digite sua renda: '))
valor_casa = float(input('Digite o valor da casa: R$'))
anos = int(input('Digite em quantos anos pretende pagar: '))
print('--=--' *20)

print('PROCESSANDO...')
sleep (2)

if idade < 18 or (valor_casa / (anos*12)) <= 0.3*renda:
    print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não se enquadra nos critérios desse empréstimo.')

else:
    prestacao_mensal = valor_casa / (anos*12)
    if renda < 1500:
        print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não tem base financeira para solicitar esse empréstimo.')

    elif renda > 50000 and prestacao_mensal <= 0.3*renda:
        print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não necessita solicitar esse empréstimo.')
        
    elif renda > 20000 and renda <= 50000 and prestacao_mensal <= 0.3*renda:
        print('\033[41;1;32m Parabéns, empréstimo aprovado! \033[m Te encaminharemos para a revisão humana.')

    elif renda >= 1500 and renda <= 20000 and prestacao_mensal <= 0.3*renda:
        print('\033[41;1;32m Parabéns, empréstimo aprovado! \033[m Te encaminharemos para o setor automatizado.')
        
    else:
        print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não se enquadra nos critérios desse empréstimo.')

print('--=--' *20)