#Programa contendo dobro, triplo e raiz quadrada
valor = int(input('Digite um valor: '))
raiz = float(valor) ** 0.5  #ou então (1/2)
print('O valor é {} \nO dobro é {} \nO triplo é {} \nA raiz quadrada é {:.2f}'.format(valor, valor*2, valor*3, raiz))

#Programa de Raiz quadrada utilizando sqrt
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}.'.format(num, raiz))

#Programa de Soma
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2

print('\n A soma é {} \n O produto é {} \n A divisão é {:.1f}'.format(s, m, d), end=' ')

print('\n A divisão inteira é {} \n A potência é {}'.format(di, e))

#Programa para saber antecessor e sucessor de um número
valor = int(input('Digite um valor: '))

print('Esse valor é {}, seu sucessor é {} e seu antecessor é {}'.format(valor, valor+1, valor-1))