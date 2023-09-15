'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo ue voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o Cosseno de {}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem tangente de {:.2f}'.format(angulo, tangente))