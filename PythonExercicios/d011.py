alt = float(input('Qual a altura da parede?\n'))
larg = float(input('Qual a largura da parede?\n'))
area = alt * larg
print(f'A área da parede é de {area}m². \nPara pintá-la serão necessários {area / 2:.2f}L de tinta.')
