'''import math
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, math.trunc(n)))'''

'''OU'''

from math import trunc
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))