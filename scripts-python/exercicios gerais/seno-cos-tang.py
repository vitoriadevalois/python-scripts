#Programa lendo ângulo qualquer e mostrando na tela o valor do Seno, Cosseno e Tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))
print('-' * 40)

#Importante de math os elementos radians, sin, cos, tan faremos:
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))