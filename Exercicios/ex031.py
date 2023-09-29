'''
Desenvolva um programa que pergunte a distancia de uma viajem em Km.
Calcule o preço da passage, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está preste a começar uma viagem de {}Km. ')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))