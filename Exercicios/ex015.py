km = float(input('Quantos KM você percorreu ? \n'))
dia = float(input('Por quantos dias o carro ficou alugado? \n'))
vdia = dia * 60
vkm = km * 0.15
print('Valor em Km {} e valor em dias {:.2f}'.format(vdia, vkm))
print('Valor total {}'.format(vdia + vkm))
