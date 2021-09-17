peso = float(input('QUal é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altua? (m) ' ))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= 18.5 < 25:
    print('Parabéns, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPRESO')