#Programa (Condições), computador pensando em um número entre 0 e 5 para o usuário adivinhar.

from random import randint
número = randint(0, 5) #O computador sorteia um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar

if jogador == número:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('Ganhei de você, humano! Eu pensei no número {} e não no {}!'.format(número, jogador))

print('-' * 40)

#Programa Multa de trânsito:
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h.')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')

print('-' * 40)

#Programa Par ou Impar:
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('{} é um número par.'.format(numero))
else:
    print('{} é um número ímpar.'.format(numero))

print('-' * 40)

#Programa Custo da Viagem:
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua pasasgem sera de R${:.2f}'.format(preço))

print('-' * 40)

#Programa Ano Bissexto:
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

print('-' * 40)

#Programa lendo 3 números
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

print('-' * 40)

#Verificando quem é o menor:
menor = a 

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print('-' * 40)

#Verificando quem é o maior:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitador foi {}'.format(maior))

print('-' * 40)

#Aumento salarial
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else: 
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

print('-' * 40)

#Analisando Triângulos
#Cada um dos segmentos devem ser menor do que a soma do comprimento dos outros dois.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulos')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')