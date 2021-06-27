#Programa que lê o ano de nascimento de sete pessoas. No final, mostra quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc

    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))