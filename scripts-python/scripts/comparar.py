# Programa que leia dois números inteiros e compara mostrando na tela qual é menor, maior e se são iguais.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O {}PRIMEIRO{} valor é maior'.format('\033[32m','\033[m'))
elif n2 > n1:
    print('O SEGUNDO valor é maior')
elif n1 == n2: #ou colocar else
    print('Os {}dois{} valores são IGUAIS'.format('\033[32m','\033[m'))
