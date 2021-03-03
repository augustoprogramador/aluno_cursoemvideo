medida = float(input('Digite uma medida: '))
print(f'A medida de {medida}m equivale a '
      f'\n{medida / 1000}km \n{medida / 100}hm.'
      f'\n{medida / 10}dam \n{medida * 10:.0f}dm.'
      f'\n{medida * 100:.0f}cm \n{medida * 1000:.0f}mm.')
