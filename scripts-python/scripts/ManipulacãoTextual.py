#MANIPULANDO TEXTOS

#FATIAMENTO
#Entre colchetes colocamos o número, referente a lacuna reservada na memória do computador, que queremos na tela.
frase = input('Digite uma frase: ')
print(frase[2])

#ANÁLISE
#Para quantar o comprimento de uma frase:
len(frase)

#Análise de quantas vezes aparece tal elemento, exemplo letra O:
frase.count('o')

#Análise de quantas vezes aparece tal elemento, exemplo letra O, com fatiamento entre 0 e 13:
frase.count('o', 0, 13)

#Quantas vezes encontrou determinado elemento
frase.find('tal elemento')

#Obs.: Se o valor devolvido for -1 = não foi encontrado.

#TRANSFORMAÇÃO
frase.replace('tal elemento', 'por tal')

#Letras minúsculas viram maiúsculas
frase.upper()

#Letras maiúsculas viram minúsculas
frase.lower()

#Só o primeiro caractere fica maiúsculo.
frase.capitalize()

#Analisa quantas palavras tem a partir dos espaços e fará o capitaliza de cada palavra.
frase.title()

#Remover espaços inúteis
frase.strip()

#Remover os últimos espaços do lado right
frase.rstrip()

#Remover os primeiros espaços do lado esquerdo
frase.lstrip()

#DIVISÃO
#Gera uma lista com todas as palavras numa cadeia de caracteres.
frase.split()

#JUNÇÃO
#Junção das frases por -
'-'.join(frase)