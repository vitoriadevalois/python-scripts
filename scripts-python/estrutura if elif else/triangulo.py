#Programa que mostra se um triângulo é equilátero, isósceles ou escaleno.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODEM{} formar um triângulo '.format('\033[32m', '\033[m'), end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os semmentos acima {}NÃO{} PODEM formar triângulo!'.format('\033[31m','\033[m'))