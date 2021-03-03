dist = float(input('Digite a distância da viagem: '))
passagem = float(0.45 * dist) if dist - 200 > 0 else float(0.5 * dist)
print(f'Valor da passagem: R${passagem:.2f}')
