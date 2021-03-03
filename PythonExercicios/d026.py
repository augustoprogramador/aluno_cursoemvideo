
'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A
Em que posição ela aparece pela primeira vez
Em que posição ela aparece pela úlima vez.'''
frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {frase.count("a")}x na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("a") + 1}')
print(f'A última letra A apareceu na posição {frase.rfind("a") + 1}')

# correção
# frase = str(input('Digite uma frase: '))
# print(f'')
