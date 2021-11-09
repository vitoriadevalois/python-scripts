#Programa para separar um número de 4 digitos em unidade, dezena, centena e milhar.
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centeza: {}'.format(c))
print('Milhar: {}'.format(m))