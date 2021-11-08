#Programa para aumento com porcentagem sobre o valor digitado
salário = float(input('Qual é o salário do funcionário? '))
novo = salário + (salário * 15/100)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
print('-' * 40)

#Programa para diminuição com porcentagem sobre o valor digitado
preço = float(input('Qual é o preco do produto? '))
novo = preço - (preço * 5/100) #5% do preço

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))