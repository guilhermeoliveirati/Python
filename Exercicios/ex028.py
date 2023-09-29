'''
Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual o numero escolhido pelo computador.
O programa devera escrever na tela se o usuario venceu ou perdeu.
'''

from random import randint
from time import sleep
computador = randint(0, 5)# Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))# Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if  jogador == computador:
    print('PARAÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))