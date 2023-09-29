'''
Faça um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salario superior a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%
'''
sal = float(input('Digite o seu salario: R$'))
if sal <= 1250:
    novosal = sal + (sal * 15 / 100)
else:
    novosal = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(sal, novosal))