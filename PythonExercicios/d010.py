dindim = float(input('Quantos reais você tem?\n'))
doleta = float(input('Qual a cotação do dólar?\n'))
# euro = float(input('Qual a cotação do euro?\n'))
print(f'Com essa quantia você pode comprar US${dindim / doleta:.2f}.')
