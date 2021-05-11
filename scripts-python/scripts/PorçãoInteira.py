#Programa para mostrar a porção inteira de um número solicitado.
import math
num = float(input('Digite um número: '))

print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))

#ou

num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))