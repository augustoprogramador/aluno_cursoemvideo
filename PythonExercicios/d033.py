# a = int(input('Digite o 1º valor: '))
# b = int(input('Digite o 2º valor: '))
# c = int(input('Digite o 3º valor: '))
# if (a > b) & (a > c):
#     print('A é o maior de todos!')
#     if b > c:
#         print('C é o menor de todos!')
#     else:
#         print('B é o menor de todos!')
# elif (b > a) & (b > c):
#     print('B é o maior de todos!')
#     if a > c:
#         print('C é o menor de todos!')
#     else:
#         print('A é o menor de todos!')
# else:
#     print('C é o maior de todos!')
#     if a > b:
#         print('B é o menor de todos!')
#     else:
#         print('A é o menor de todos!')

# correção
a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')
