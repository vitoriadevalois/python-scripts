#Programa que lê o primeiro termo e a razão de uma PA (progressão aritmética).No final, mostrando os 10 primeiros termos dessa progressão, utilizando while. O programa pergunta se o usuário quer mostrar mais alguns termos e encerra quando o usuário disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais 
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))