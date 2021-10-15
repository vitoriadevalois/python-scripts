#Programa jogo de adivinhação com o computador.

import random
total_de_tentativas = 10
pontos = 1000

def jogar():
    print('{}*{}'.format('\033[35m', '\033[m') * 55)
    nome = input('Digite seu nome: ')
    print('Bem-vind@ ao jogo da adivinhação, {}{}{}'.format('\033[36m', nome, '\033[m'))
    print('{}*{}'.format('\033[35m', '\033[m') * 55)

    print('Escolha uma dificuldade:')
    dificuldade = int(input(' Digite [1] para FÁCIL (1 a 10). \n Digite [2] para MÉDIO (1 a 50). \n Digite [3] para DIFÍCIL (1 a 100). \n Digite sua escolha: '))
    print('{}*{}'.format('\033[35m', '\033[m') * 55)

    if dificuldade == 1:
        numero_secreto = random.randint(1, 10)
        print('Você selecionou a dificuldade {}FÁCIL{}... Está com medinho de uma máquina?'.format('\033[32m', '\033[m'), numero_secreto)
        for rodada in range(1, total_de_tentativas + 1):
            print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
            chute_str = input('Digite um número entre 1 e 10: ')
            print('{}Você digitou:{} {}'.format('\033[36m', '\033[m', chute_str))
            chute = int(chute_str)

            if(chute < 1 or chute > 10):
                print('Você deve digitar um número entre 1 e 10!')
                continue

            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print('{}Você me venceu com {} pontos, humano... Parabéns.{}'.format('\033[32m', pontos ,'\033[m'))
                break
            else:
                if (maior):
                    print('{}Você errou!{} O seu chute foi maior que o número secreto.'.format('\033[31m','\033[m'))
                    print('{}*{}'.format('\033[35m', '\033[m') * 55)
                    if (rodada == 10):
                        print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                elif (menor):
                    print('Você errou! O seu chute foi menor que o número secreto.')
                    print('{}*{}'.format('\033[35m', '\033[m') * 55)
                    if (rodada == 10):
                        print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    if dificuldade == 2:
        numero_secreto = random.randint(1, 50)
        print('Você selecionou a dificuldade {}MÉDIA{}... Interessante.'.format('\033[33m','\033[m'))
        for rodada in range(1, total_de_tentativas + 1):
            print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
            chute_str = input('Digite um número entre 1 e 50: ')
            print('{}Você digitou:{} {}'.format('\033[36m', '\033[m', chute_str))
            chute = int(chute_str)

            if(chute < 1 or chute > 50):
                print('Você deve digitar um número entre 1 e 50!')
                continue

            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print('{}Você me venceu com {} pontos, humano... Parabéns.{}'.format('\033[32m', pontos ,'\033[m'))
                break
            else:
                if (maior):
                    print('{}Você errou!{} O seu chute foi maior que o número secreto.'.format('\033[31m','\033[m'))
                    print('{}*{}'.format('\033[35m', '\033[m') * 55)
                    if (rodada == 10):
                        print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                elif (menor):
                    print('Você errou! O seu chute foi menor que o número secreto.')
                    print('{}*{}'.format('\033[35m', '\033[m') * 55)
                    if (rodada == 10):
                        print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    if dificuldade == 3:
        numero_secreto = random.randint(1, 100)
        print('Você provavelmente perdeu a cabeça e escolheu o modo {}DIFÍCIL{}. QUAL É O SEU PROBLEMA? Ok, tudo bem... você nunca vai me vencer.'.format('\033[31m','\033[m'))
        for rodada in range(1, total_de_tentativas + 1):
            print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
            chute_str = input('Digite um número entre 1 e 100: ')
            print('{}Você digitou:{} {}'.format('\033[36m', '\033[m', chute_str))
            chute = int(chute_str)

            if(chute < 1 or chute > 100):
                print('Você deve digitar um número entre 1 e 100!')
                continue

            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print('{}Você me venceu com {} pontos, humano... Parabéns.{}'.format('\033[32m', pontos ,'\033[m'))
                break
            else:
                if (maior):
                    print('{}Você errou!{} O seu chute foi maior que o número secreto.'.format('\033[31m','\033[m'))
                    print('{}*{}'.format('\033[35m', '\033[m') * 55)
                    if (rodada == 10):
                        print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                elif (menor):
                    print('{}Você errou!{} O seu chute foi menor que o número secreto.'.format('\033[31m','\033[m'))
                    print('{}*{}'.format('\033[35m', '\033[m') * 55)
                    if (rodada == 10):
                        print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print('Fim do jogo')