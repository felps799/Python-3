import random
lista_alunos = []
while True:
    nome_aluno = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome_aluno.lower() == 'sair':
        break
    lista_alunos.append(nome_aluno)

print(f"Lista de alunos: {lista_alunos}")
print(f"A ordem de apresentação é: {random.sample(lista_alunos, len(lista_alunos))}")