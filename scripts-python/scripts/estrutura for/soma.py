#Programa que calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo desejado pelo usuário.
soma = 0
cont = 0
i = int(input('Digite o valor máximo desejado: '))
for c in range(1, i+1, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))