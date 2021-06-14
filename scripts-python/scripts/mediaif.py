#Programa que lê duas notas de um aluno, calcula a média e mostra uma mensagem.

nome = str(input('Qual é o nome do aluno? '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno {}{}{} é {:.1f}.'.format(nota1, nota2, '\033[34m', nome, '\033[m', media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')