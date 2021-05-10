nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma = nota1 + nota2

print('A média do aluno {} é {:.1f}'.format(nome, soma/2))