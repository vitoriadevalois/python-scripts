#Programa para leitura do comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, mostrando o comprimento da hipotenusa.

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 0.5

print(' A hipotenusa vai medir {:.2f}'.format(hi))
print('-' * 40)

#Programa para leitura do comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, mostrando o comprimento da hipotenusa utilizando a importação da classe math
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

print(' A hipotenusa vai medir {:.2f}'.format(hi))
