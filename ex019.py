# um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
lista_alunos = []
while True:
    nome_aluno = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome_aluno.lower() == 'sair':
        break
    lista_alunos.append(nome_aluno)

print(f"Lista de alunos: {lista_alunos}")
print(f"O aluno escolhido para apagar o quadro é: {random.choice(lista_alunos)}")