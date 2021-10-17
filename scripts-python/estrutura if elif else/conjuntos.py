#Organizando conjntos e subconjuntos de elementos em Python

conjunto = {1, 2, 3, 4, 5} 
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2) #com .union criamos a união entre conjuntos
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2) #com .intersection podemos saber o que existe em ambos os conjuntos
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2) #com .difference podemos saber o que existe de diferença no conjunto 2 perante o conjunto 1.
conjunto_diferenca2 = conjunto2.difference(conjunto) #com .difference podemos saber o que existe de diferença no conjunto 1 perante o conjunto 2.
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2) #com .symetric_difference podemos saber a diferença simétrica entre os conjuntos.
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

#Descobrindo o subset (subconjunto)
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_a)
print('O conjunto A é um conjunto subset do conjunto B?: {}'.format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('O conjunto B é um conjunto subset do conjunto A?: {}'.format(conjunto_subset))

#Descobrindo o superset (supraconjunto)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('O conjunto B é um conjunto superset (supraconjunto) do conjunto A?: {}'.format(conjunto_superset))
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('O conjunto A é um conjunto superset (supraconjunto) do conjunto B?: {}'.format(conjunto_superset))

#Como converter uma lista em conjunto
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)

#Como converter conjunto em lista
lista_naimais = list(conjunto_animais)
print(lista_naimais)

# Outras funções:
# conjunto.add(5)  #para adicionar um elemento no conjunto
# conjunto.discard(2) #para remover um elemento no conjunto