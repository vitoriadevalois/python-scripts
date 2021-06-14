#Programa que lê um número inteiro qualquer e peça pro usuário escolher qual será a base de conversão desejada

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else: print('Opção inválida. Tente novamente.')

# O resultado conterá:
# 0b -> para opção binária.
# 0o -> para opção octal.
# 0x -> para opção hexadecimal.