sal = float(input('Informe o seu salário: '))
if sal > 1250:
    print(f'Seu salário recebeu reajuste de 10%.\nSeu novo salário é de R${sal * 1.1:.2f}')
else:
    print(f'Seu salário recebeu reajuste de 15%.\nSeu novo salário é de R${sal * 1.15:.2f}')
