n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2

print('\n A soma é {} \n O produto é {} \n A divisão é {:.1f}'.format(s, m, d), end=' ')

print('\n A divisão inteira é {} \n A potência é {}'.format(di, e))
