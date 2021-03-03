from math import cos, sin, tan, radians
ang = int(input('Digite um ângulo: '))

# É NECESSÁRIO CONVERTER

print(f'O seno de {ang}º vale {sin(radians(ang)):.2f}')
print(f'O cosseno de {ang}º vale {cos(radians(ang)):.2f}')
print(f'A tangente de {ang}º vale {tan(radians(ang)):.2f}')
