'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
STRIP é para remover os espaços
UPPER é para criar uma cópia de uma string com todas as letras minúsculas convertidas em letras maiúsculas
'''

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))