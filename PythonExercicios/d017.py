'''from math import hypot
cat1 = float(input('Digite o primeiro cateto: '))
cat2 = float(input('Digite o segundo cateto: '))
print(f'A hipotenusa mede {hypot(cat1, cat2):.2f}')
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
print(f'A hipotenusa vai medir {(co ** 2 + ca ** 2) ** (1/2):.2f}')
