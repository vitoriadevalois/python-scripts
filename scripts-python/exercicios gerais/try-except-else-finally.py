# Gerenciando e criando exceções customizadas com try, except, else e finally.
# Consulte https://docs.python.org/3/library/exceptions.html#exception-context para saber a hierarquia das exceções (exception hierarchy)

lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    print('fechando arquivo')
    arquivo.close()
    
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero.')   
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()