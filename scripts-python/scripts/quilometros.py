#Programa para saber o total a se pagar sobre um carro alugado de acordo com dias e km rodados.
dias = int(input('Quantos dias alugado: '))
km = float(input('Quantos km rodados: '))
pago = dias * 60 + (km * 0.15)
import emoji

print(emoji.emojize('O total a pagar é de R${:.2f} :smile:'.format(pago)))