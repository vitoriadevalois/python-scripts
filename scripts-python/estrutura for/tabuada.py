#Programa para gerar uma tabuada, utilizando estrutura for, conforme o número que o usuário deseja.
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
