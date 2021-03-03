vel = int(input('Qual a sua velocidade?\n'))
vel -= 80
if vel > 0:
    print(f'Você ulrapassou o limite de velocidade e foi multado em R${float(7 * vel):.2f}')
