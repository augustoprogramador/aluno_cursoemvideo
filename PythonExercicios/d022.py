# nome = input('Digite seu nome completo: ')
# print(f'Seu nome em maiúsculo é {nome.upper()}')
# print(f'Seu nome em minúsculo é {nome.lower()}')
# print(f'Seu nome completo possui {len(nome.replace(" ", ""))} letras.')
# print(f'Seu primeiro nome tem {len(nome.split()[0])} letras.')

# correção
print('CORREÇÃO!!!')
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome completo possui {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
# print(f'Seu primeiro nome tem {len(nome.split()[0])} letras.')
