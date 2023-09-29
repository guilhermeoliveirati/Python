'''
Crie um programa que leia um numero inteiro e mostre na tela se ele é par pu impar
'''
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2 #o resto da divisão do numero por dois
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))