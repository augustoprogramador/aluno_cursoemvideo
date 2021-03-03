'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.'''
nome = str(input('Digite seu nome completo: ')).lower().strip()
print(f'Você {"possui" if nome.find("silva") > -1 else "não possui"} Silva no nome.')

# correção
nome = str(input('Qual é seu nome completo? '))
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')
