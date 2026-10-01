salario = float(input('Digite seu salário: '))
print('-=-' *50)
if salario > 1250.00:
    print(f'Seu aumento de 10% reajustará seu salário de {salario} para {salario + salario*0.1}')
if salario <= 1250.00:
    print(f'Seu aumento de 15% reajustará seu salário de {salario} para {salario + salario*0.15}')
print('-=-' *50)