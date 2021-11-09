#Programa para conversão de reais em dólares de acordo com a cotação implicada
reais = float(input('Digite o valor em reais: '))
cotacao = float(input ("Informe o valor da cotação do dólar: "))

print('R${} = U$ {:.2f}'.format(reais, reais / cotacao))