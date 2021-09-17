#Programa exemplificando condição aninhada, verificando nomes e exibindo respostas diferentes.

nome = str(input('Qual é o seu nome? '))
if nome == 'Vitória':
    print('Que nome incrível você tem.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino você tem')
else:
    print('Que nome comum...')
print('Prazer em te conhecer {}{}{}'.format('\033[1;35m', nome, '\033[1;35m'))