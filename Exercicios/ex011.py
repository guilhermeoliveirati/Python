largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
print('A sua parede tem a dimensão {} X {} e sua área é de {}m2.'.format(largura, altura, area))

tinta = area / 2
print('Para pintar a parece voce vai precisar de {}L.'.format(tinta))
