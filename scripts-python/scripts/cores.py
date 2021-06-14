print('\033[31mOlá, Mundo!') #Vermelho
print('\033[32mOlá, Mundo!') #Verde
print('\033[33mOlá, Mundo!') #Amarelo
print('\033[34mOlá, Mundo!') #Azul
print('\033[35mOlá, Mundo!') #Roxo
print('\033[36mOlá, Mundo!') #AzulCiano
print('\033[37mOlá, Mundo!') #Branco

print('\033[0;30;40mOlá, Mundo!') #Preto
print('\033[1;31;44mOlá, Mundo!\033[m') #Fundo Azul
print('\033[4;32;43mOlá, Mundo!\033[m') #Fundo Amarelo
print('\033[7;34;42mOlá, Mundo!\033[m') #Fundo AzulEscuro
print('\033[7;40;40mOlá, Mundo!\033[m') #Fundo Branco
print('\033[0;35;46mOlá, Mundo!\033[m') #Fundo Pandemia
print('\033[0;36;45mOlá, Mundo!\033[m') #Fundo Rosa

nome = input('Qual é o seu nome? ')
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[1;35m', nome, '\033[m'))

#Para inserir apenas em um local utilizar {} e fechar com \033[m