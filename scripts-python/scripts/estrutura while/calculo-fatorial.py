#Programa que leia um número qualquer e mostre o seu fatorial, utilizando método de cálculo fatorial.
from math import factorial
n = int(input('Digite um número para calcular seu Fatoria: '))
f = factorial(n)
print('O faotorial de {} é {}.'.format(n, f))