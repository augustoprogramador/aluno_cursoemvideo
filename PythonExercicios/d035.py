a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a > b >= c:
    print(f'{"É um triângulo" if b + c > a else "Não é um triângulo."}')
elif b > a >= c:
    print(f'{"É um triângulo" if a + c > b else "Não é um triângulo."}')
else:
    print(f'{"É um triângulo" if b + a > c else "Não é um triângulo."}')
