#Programa que lê vários números inteiros. No final da execução, mostra a média entre todos os valores e qual foi o MAIOR e o MENOS valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores.
resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}. O maior número é {} e o menor número é {}!'.format(quantidade, media, maior, menor))