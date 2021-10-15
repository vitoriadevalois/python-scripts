#Programa para leitura do comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, mostrando o comprimento da hipotenusa utilizando a importação da classe math
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

print(' A hipotenusa vai medir {:.2f}'.format(hi))
