from random import randint, choice
nome = [] * 4
# nome.append('t1')
# nome.append('t2')
# nome.append('t3')
# nome.append('t4')
for x in range(0, 4):
    nome.append(input('Digite o nome do aluno: '))
# print(f'O sorteado para apagar o quadro foi {nome[randint(0, 3)]}!')
print(f'O sorteado para apagar o quadro foi {choice(nome)}!')
