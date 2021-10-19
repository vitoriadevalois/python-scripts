#Programa que leia o nome completo e mostra quantas letras ao todo, quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Programa que lê o nome completo de uma pessoa e mostra o primeiro e último nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
