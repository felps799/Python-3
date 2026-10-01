s = float(input("Qual é o salário do funcionário? R$ "))
r = float(input("Qual é a porcentagem de aumento? "))
print(f"O salário do funcionário era de R${s:.2f} e com {r}% de aumento, passará a ser R${s + (s * r /100):.2f}.")