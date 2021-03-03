from random import randint, choice, shuffle
aluno = []
for x in range(0, 4):
    aluno.append(input('Informe o nome do aluno: '))
shuffle(aluno)
for x in range(0, 4):
    print(f'{aluno[x]} se apresentará em {x + 1}º lugar')
