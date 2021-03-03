'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''

from random import randint
# n = str(randint(0, 9999))
# u = d = c = m = 0
# print(n)
# print(f'Unidadde: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}')

# n = randint(0, 9999)
n = int(input('Digite um número: '))
print(n)
print(f'Unidade: {n % 10}'
      f'\nDezena: {n // 10 % 10}'
      f'\nCentena: {n // 100 % 10}'
      f'\nMilhar: {n // 1000 % 10}')
