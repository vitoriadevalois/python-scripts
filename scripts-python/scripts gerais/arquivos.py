#Como gerar, copiar, mover, escrever e ler informações de arquivos externos
import shutil

open('teste.txt', 'w') #tipo w de write, se ele não existe ele gera, e se já está escrito ele irá sobrepor o arquivo.

def escrever_arquivo(texto):
    # diretorio = 'escrever o diretório'  #para colocar num diretório específico
    # arquivo = open(diretorio, 'w')
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open('notas.txt', 'a') #caso seja um arquivo que já exista e há necessidade de atualizar, usamos 'a'.
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open('notas.txt', 'r') #tipo r de read, para ler o arquivo.
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open('notas.txt', 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #split para inserir numa lista
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        print(x)
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4 #fazendo o for, retornando a lista para inteiro e exibindo a média
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

# COMO COPIAR UM ARQUIVO
# def copia_arquivo(nome_arquivo):  
#     shutil.copy(nome_arquivo, 'local para ser copiado')

#COMO MOVER UM ARQUIVO
# def move_arquivo(nome_arquivo):
#     shutil.move(nome_arquivo, 'local para ser movido')

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
# if __name__ == '__main__':
#     escrever_arquivo('Primeira linha.\n')
#     aluno = 'Fernanda,10,4,5,8\n'
#     atualizar_arquivo('notas.txt', aluno) #para atualizar o arquivo, apenas modificamos o texto que vem aqui.
#     ler_arquivo('teste.txt')