reais = float(input('Digite o valor em reais: '))
cotacao = float(input ("Informe o valor da cotação do dólar: "))

print('R${} = U$ {:.2f}'.format(reais, reais / cotacao))