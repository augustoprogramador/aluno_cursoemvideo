i = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(i)}')
print(f'É alfanumérico? {i.isalnum()}')
print('É alfabético?', i.isalpha())
# print(f'É ASCII? {i.isascii()}')
# print('É um dígito?', i.isdigit())
print(f'Está em minúsculo? {i.islower()}')
print('É decimal?', i.isdecimal())
print(f'É identificador? {i.isidentifier()}')
print('É numérico?', i.isnumeric())
print(f'É possível imprimir? {i.isprintable()}')
print('Possui apenas espaços?', i.isspace())
print(f'Está capitalizado? {i.istitle()}')
print('Está em maiúsculo?', i.isupper())
