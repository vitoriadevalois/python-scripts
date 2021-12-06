  # <p align="center"> 💻 Anotações e Informações Úteis 💻
  [![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)

## ✅ ATALHOS VSCODE
 
 | Função | Atalho |
 | --- | --- |
 | Localizar e Substituir | CRTL + H |
 | Abrir uma abreviação | CRTL + SHIFT + P (Selecionar Emmet: Wrap With Abbreviation) |
 | Adicionar comentário em linhas selecionadas | CRTL + ; |

## ✅ TIPOS DE VARIÁVEL PYTHON

 ▫️ int -> (7, -4, 0, 9843)
 
 ▫️ float -> (4.023, -15.323)
 
 ▫️ bool -> (True or False)
 
 ▫️ str -> ("Olá", "7.5" "")

 ## ✅ CONDIÇÕES
 São elas: if, elif, else, while, for.
 
 ▫️ IF -> Utilizamos o comando if para verificar uma expressão e executar um bloco de código caso a condição definida seja verdadeira. É importante dizer que a instrução if pode ser utilizada sozinha, ou seja, apenas para executar algo se a condição for verdadeira. Observe que devemos utilizar o caractere dois pontos “:” ao final da instrução.
 
 ▫️ ELIF -> O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa. 

 `if (expressão_for_verdadeira):
    executar_primeiro_bloco_de_codigo()
elseif (segunda_expressão_for_verdadeira):
    executar_segundo_bloco_de_codigo()`
 
 ▫️ ELSE -> O comando else é utilizado para executar um bloco de código, caso o resultado da expressão informada na instrução if seja falso. Vale ressaltar que a instrução else só pode ser utilizada em conjunto com o if. Perceba que também precisamos utilizar o caractere dois pontos após a expressão da instrução if e após o else.

`if (expressão_for_verdadeira):
    executar_primeiro_bloco_de_codigo()
else:
    executar_segundo_bloco_de_codigo()`

 WHILE -> Laço usado como "looping", enquanto tal coisa estiver acontecendo então...

`contador = 0
while (contador < 5):
       print(contador)
       contador   = contador + 1`
 
 FOR -> Este laço utiliza uma variável para controlar a contagem do loop, bem como seu incremento. Trata-se de um comando bem enxuto, já que própria estrutura faz a inicialização, incremento e encerramento do laço.

A estrutura for pode ser exemplificada como: 

`for c in range(0, 6, 2):
    print(c)
print('Fim!')`
     
  > Diferença While e For:
  > 
  > Sabendo o LIMITE (um valor máximo) então podemos usar FOR ou WHILE.
  > 
  > Se não sabemos o LIMITE então usamos WHILE até que seja atingido o limite desejado pelo usuário.

WHILE -> O comando while faz com que um conjunto de instruções seja executado enquanto uma condição é atendida. Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida, como mostra o exemplo a seguir:

`contador = 0
while (contador < 5):
       print(contador)
       contador   = contador + 1`

Neste código, enquanto a variável contador, inicializada com 0, for menor do que 5, as instruções das linhas 3 e 4 serão executadas.


WHILE-ELSE -> Ao final do while podemos utilizar a instrução else. O propósito disso é executar alguma instrução ou bloco de código ao final do loop, como podemos ver no exemplo a seguir:

`contador = 0
while (contador < 5):
      print(contador)
      contador = contador + 1
else:
      print("O loop while foi encerrado com sucesso!")`

Assim como acontece com for/else, declarando o else ao final do while é possível executar um código ao final do loop. Neste caso será impressa a mensagem: “O loop while foi encerrado com sucesso!”.

## ✅ BREAK
 É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
 
## ✅ BÁSICO

 ▫️ print -> (exprimir algo na tela)
 
 ▫️ is -> is alguma coisa, saber se é ou não true or false
 
 ▫️ {} -> format para inserir no meio da frase alguma variavel
 
 ▫️ != = diferente / não-igual

 Ex.: 
 
 `print("É um prazer te conhecer, {}!".format(nome))
 int(input('valor que recebe número inteiro))`

## ✅ OPERADORES ARITMÉTICOS

 ▫️ + Adicção
 
 ▫️ - Subtração
 
 ▫️ * Multiplicação
 
 ▫️ / Divisão (float division)
 
 ▫️ ** Potência
 
 ▫️ // Divisão Inteira (integer division)
 
 ▫️ % Resto da Divisão

## ✅ OPERADORES DE COMPARAÇÃO
 
 ▫️ < - menor que
 
 ▫️ > - maior que
 
 ▫️ <= - menor ou igual a
 
 ▫️ >= - maior ou igual a
 
 ▫️ == - igual a
 
 ▫️ != - diferente de

## ✅ ORDEM DE PRECEDÊNCIA
 ▫️ 1º ()
 
 ▫️ 2º ** potências 
 
 ▫️ 3º * / // %
 
 ▫️ 4º + - 

## ✅ ALINHAMENTO

 `nome = input('Qual seu nome? ')
 
 print('Prazer em conhecer {:=^20}'.format(nome))`

 - Aparecer em 20 caracteres usando :20
 
 `print('Prazer em te conhecer {:20}!'.format(nome))`

 - Alinhamento à direita coloca >
 
 `print('Prazer em te conhecer {:>20}!'.format(nome))`

 - Alinhamento à esquerda coloca <
 
 `print('Prazer em te conhecer {:<20}!'.format(nome))`

 - Alinhamento centralizado coloca ^
 
 `print('Prazer em te conhecer {:^20}!'.format(nome))`

 - Alinhamento com caracteres nos espaços 
 
 `print('Prazer em te conhecer {:=^20}!'.format(nome))`

 ## ✅ IMPORTAR ITENS
 
 `import [bebida]` (vai importar tudo de bebida)
 
 `from [bebida] import cafe` (vai importar apenas o café das bebidas)

## ✅ BIBLIOTECAS
 Link com as bibliotecas python: https://docs.python.org/3/library/math.html
 
## ✅ BIBLIOTECA MATH

 ▫️ ceil -> (arredondamento pra cima)
 
 ▫️ floor -> (arredondamento pra baixo)
 
 ▫️ trunc -> (eliminar da virgula da frente)
 
 ▫️ pow -> (potência)
 
 ▫️ sqrt -> (raiz quadrada)
 
 ▫️ factorial -> (fatorial de um numero)

## ✅ IMPORTAÇÃO
 Utilizar import (nome da biblioteca)
 
 Exemplo: se precisar de um calculo só de raiz quadrada, então: `from math import sqrt`

## ✅ CORES NO TERMINAL

 \033[ style  text   back m

 \033[0;33;44m
 style 0 -> sem estilo
 33 -> texto
 44 -> back

## ✅ TABELA DE CORES LETRAS NO TERMINAL

 ▫️ \033[31m Vermelho
 
 ▫️ \033[32m Verde
 
 ▫️ \033[33m Amarelo
 
 ▫️ \033[34m Azul
 
 ▫️ \033[35m Roxo
 
 ▫️ \033[36m AzulCiano
 
 ▫️ \033[37m Branco
 
 ▫️ \033[0;30;40m Preto
 
 (Para inserir apenas em um local utilizar {} e fechar com \033[m)

## ✅ TABELA DE CORES FUNDO NO TERMINAL

 ▫️ \033[1;31;44mOlá Fundo Azul
 
 ▫️ \033[4;32;43mOlá Fundo Amarelo
 
 ▫️ \033[7;34;42mOlá Fundo AzulEscuro
 
 ▫️ \033[7;40;40mOlá Fundo Branco
 
 ▫️ \033[0;35;46mOlá Fundo Pandemia
 
 ▫️ \033[0;36;45mOlá Fundo Rosa
 
 (Para inserir apenas em um local utilizar {} e fechar com \033[m)

## ✅ ESTILOS NO TERMINAL
 
 0 -> nenhum
 
 1 -> negrito
 
 4 -> sublinhado
 
 7 -> negativo

## ✅ SUBSTITUIR CORES VOCÊ MESMO
 
 Text:
 
 ▫️ 30 branco
 
 ▫️ 31 vermelho
 
 ▫️ 32 verdadeiro
 
 ▫️ 33 amarelo
 
 ▫️ 34 azul
 
 ▫️ 35 roxo
 
 ▫️ 36 azul ciano
 
 ▫️ 37 cinza (padrão)

 Back (fundo):
 
 ▫️ 40 branco
 
 ▫️ 41 vermelho
 
 ▫️ 42 verde 
 
 ▫️ 43 amarelo
 
 ▫️44 azul
 
 ▫️ 45 roxo
 
 ▫️ 46 azul ciano 
 
 ▫️ 47 cinza 

## ✅ FORMATAÇÃO DE STRING
 https://docs.python.org/3/library/string.html#formatexamples

## ✅ BUILTIN FUNCTIONS (funções embutidas)
 https://docs.python.org/3/library/functions.html

## ✅ MANIPULANDO TEXTOS

 ### FATIAMENTO
 Entre colchetes colocamos o número, referente a lacuna reservada na memória do computador, que queremos na tela.
 
 `frase = input('Digite uma frase: ')
 print(frase[2])`

 ### ANÁLISE
 
 | Função | Comando |
 | --- | --- |
 | Para contar o comprimento de uma frase | `len(frase)` |
 | Análise de quantas vezes aparece tal elemento, exemplo letra O | `frase.count('o')` |
 | Análise de quantas vezes aparece tal elemento, exemplo letra O, com fatiamento entre 0 e 13 | `frase.count('o', 0, 13)` |
 | Quantas vezes encontrou determinado elemento | `frase.find('tal elemento')` |
 
 Obs.: Se o valor devolvido for -1 = não foi encontrado.

 ## ✅ TRANSFORMAÇÃO
 
 | Função | Comando |
 | --- | --- |
 | Substituir elementos | `frase.replace('tal elemento', 'por tal')` |
 | Letras minúsculas viram maiúsculas | `frase.upper()` |
 | Letras maiúsculas viram minúsculas | `frase.lower()` |
 | Só o primeiro caractere fica maiúsculo | `frase.capitalize()` |
 | Analisa quantas palavras tem a partir dos espaços e fará o capitaliza de cada palavra | `frase.title()` |
 | Remover espaços inúteis | `frase.strip()` |
 | Remover os últimos espaços do lado right | `frase.rstrip()` |
 | Remover os primeiros espaços do lado esquerdo | `frase.lstrip()` |

 ## ✅ DIVISÃO
 
 | Função | Comando |
 | --- | --- |
 | Gera uma lista com todas as palavras numa cadeia de caracteres | `frase.split()` |

 ## JUNÇÃO 💻
 
 | Função | Comando |
 | --- | --- |
 | Junção das frases por - | `'-'.join(frase)` |

 ## ✅ TIPO LIST
 
 | Função | Comando |
 | --- | --- |
 | Remove o último elemento de uma lista ou elemento da posição informada | `pop()` |
 | Remove um elemento de uma lista pelo nome do elemento | `remove()` |
 | Acrescenta um novo valor para a lista, esse valor é sempre adicionado ao final da lista | `append()` |
