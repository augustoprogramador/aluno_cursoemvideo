
'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo". '''

city = str(input('Digite o nome da cidade: ')).strip()
print(f'Sua cidade {"começa" if city[:5].lower() == "santo" else "não começa"} com Santo no nome')
