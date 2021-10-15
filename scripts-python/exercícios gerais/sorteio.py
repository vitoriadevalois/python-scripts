#Programa para sortear entre números escolhidos.
#Obs.: para fazer com letras, substitua int por str (string), randint por choose, crie outros n.

import random
n1 = int(input('Primeiro elemento: '))
n2 = int(input('Segundo elemento: '))
escolhido = random.randint(n1, n2)

print('O elemento escolhido foi {}'.format(escolhido))

#Programa para sortear a ordem entre elementos escolhidos.
from random import shuffle
n1 = input('Digite o primeiro elemento: ')
n2 = input('Digite o segundo elemento: ')
n3 = input('Digite o terceiro elemento: ')
n4 = input('Digite o terceiro elemento: ')
lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem escolhida será {}'.format(lista))
