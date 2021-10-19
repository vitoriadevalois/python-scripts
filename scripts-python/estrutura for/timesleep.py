#Programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep #importar da biblioteca "time", o termo "sleep" que é como um cochilo, uma pausa no programa.
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1) #pausa de 1 segundo
print('BUM! BUM! POOOWW!')
