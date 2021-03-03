'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Augusto Soares de Camargo
Primeiro: Augusto
Último: Camargo'''

nomeC = str(input('Digite seu nome completo: ')).strip()
nomes = nomeC.split()
print(f'Primeiro nome: {nomes[0]}\nÚltimo nome: {nomes[len(nomes)-1]}')
