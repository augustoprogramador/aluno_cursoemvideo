dias = int(input('Por quantos dias alugou o veículo?\n'))
km = float(input('Quantos KM você percorreu?\n'))
print(f'O total a pagar é de R$'
      f'{km * 0.15 + dias * 60:.2f}')
