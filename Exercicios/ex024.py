'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

STRIP é para remover os espaços
UPPER é para criar uma cópia de uma string com todas as letras minúsculas convertidas em letras maiúsculas
'''

cid = str(input('Em que cidade voce nasceu? ')). strip()
print(cid[:5].upper() == 'SANTO')