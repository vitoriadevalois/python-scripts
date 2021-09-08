#Programa que lê seis números inteiros e mostre a soma somente dos números que forem pares. Se o valor digitado for ímpar, o programa desconsidera.
soma = 0
cont = 0
for c in range (1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))