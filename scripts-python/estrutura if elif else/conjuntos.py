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

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

# conjunto.add(5)  #para adicionar um elemento no conjunto
# conjunto.discard(2) #para remover um elemento no conjunto
