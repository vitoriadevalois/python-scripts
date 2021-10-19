#Como organizar os dados em uma lista ou tupla e realizar operações com elas

lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'logo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10 ,12, 14) #tupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável. Isso significa que quando uma tupla é criada não é possível adicionar, alterar ou remover seus elementos.
tupla[0] = 12
print(len(tupla))

# if 'lobo' in lista_animal: #se tem um 'lobo' na lista' então...
#     print('Existe um lobo na lista.')
# else:
#     print('Não existe um lobo na lista. Será incluído.')
#     lista_animal.append('lobo') #o .append irá adicionar na lista o lobo
#     print(lista_animal)

# 
# lista.sort() # .sort será utilizado para colocar em ordem a lista
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse() # .reverse será utilizado para reverter

#  
# lista_animal.pop() #irá retirar a última posição da lista, dentro do parenteses podemos colocar o número contendo a posição que queremos tirar
# print(lista_animal)

# 
# lista_animal.remove('elefante') irá remover determinado elemento que já conhecemos
# print(lista_animal)